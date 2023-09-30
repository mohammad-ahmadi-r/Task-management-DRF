from django.urls import path
from .views import (
    RegisterView, 
    LoginView, 
    LogoutView,
    EmailVerificationView, 
    EmailVerificationRequestView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),    
    path('verify-email/', EmailVerificationView.as_view(), name='email-verification'),
    path('request-verification/', EmailVerificationRequestView.as_view(), name='request-verification'),
]
