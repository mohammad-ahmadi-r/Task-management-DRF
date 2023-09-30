from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class EmailVerificationSerializer(serializers.Serializer):
    token = serializers.CharField()