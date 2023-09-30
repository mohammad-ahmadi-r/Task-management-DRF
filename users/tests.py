from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        username = 'testuser'
        password = 'testpassword'
        email = 'test@example.com'

        response = self.client.post(
            reverse('register'),
            data={
                'username': username,
                'password1': password,
                'email': email
            }
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username=username).exists())

class EmailRegistrationTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = 'testpassword'
        email = 'test@example.com'

        User.objects.create_user(username=username, password=password, email=email)

    def test_email_registration(self):
        username = 'testuser'
        response = self.client.post(
            reverse('request-verification'),
            data={
                'username': username
            }
        )

        self.assertEqual(response.status_code, 200)