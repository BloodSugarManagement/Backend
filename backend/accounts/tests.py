from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser


class UserRegisterLoginTestCase(APITestCase):
    def setUp(self):
        self.user_email = "testcase@welcome.com"
        self.user_password = "testcase"

        self.url = reverse("account_signup")
        self.payload = {
            "email": self.user_email,
            "age_range": "20대",
            "password": self.user_password,
        }

    def test_registeration(self):
        """User registeration"""

        self.register_response = self.client.post(self.url, self.payload)

        self.assertEqual(self.register_response.status_code, status.HTTP_200_OK)

    def test_login(self):
        """User login"""

        user = CustomUser.objects.create_user(**self.payload)

        url = reverse("rest_login")
        payload = {
            "email": self.user_email,
            "password": self.user_password,
        }

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
