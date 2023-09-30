from django.db import models
from django.contrib.auth.models import User

class EmailVerification(models.Model):
    email_user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)