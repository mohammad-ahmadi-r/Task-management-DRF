from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from .models import EmailVerification
import secrets
from .serializers import EmailVerificationSerializer
from .tasks import user_verification_email


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)


#TODO: apply an instant logout in server-side
class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        elif User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already taken'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)


class EmailVerificationView(APIView):
    def post(self, request):
        token = request.query_params.get('token')

        try:
            verification = EmailVerification.objects.get(token=token)
        except EmailVerification.DoesNotExist:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        user = verification.email_user
        user.is_active = True
        user.save()
        verification.delete()

        return Response({'detail': 'Email verified successfully'}, status=status.HTTP_200_OK)


class EmailVerificationRequestView(APIView):
    def post(self, request):
        print(request.data)
        try:
            user = User.objects.get(username=request.data['username'])
        except:
            user = User.objects.get(email=request.data['email'])

        try:
            EmailVerification.objects.get(email_user=user).delete()
        except:
            pass

        #TODO: check if email is already verified or not
        # if user.is_active ==True:
        #     return Response({'detail': 'email already verified.'}, status=status.HTTP_200_OK)

        token = secrets.token_urlsafe(32)
        EmailVerification.objects.create(email_user=user, token=token)

        user_verification_email.delay(user.email, token)

        return Response({'detail': 'Verification link sent to your email'}, status=status.HTTP_200_OK)