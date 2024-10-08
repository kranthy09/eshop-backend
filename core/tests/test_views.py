"""
Test core app url endpoint API views
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import User


class HealthCheckTests(TestCase):
    """
    Test suite for the HealthCheckView class-based view.
    """

    def setUp(self):
        """
        Set up any state specific to the execution of the test case.
        """
        self.client = APIClient()
        self.url = reverse(
            "health-check"
        )  # Name of the health check endpoint as defined in urls.py

    def test_health_check_returns_200(self):
        """
        Test if the health check endpoint returns a 200 status code.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_health_check_response_content(self):
        """
        Test if the health check endpoint returns the expected JSON response.
        """
        response = self.client.get(self.url)
        expected_data = {
            "status": "healthy",
            "message": "The API is up and running.",
        }
        self.assertEqual(response.json(), expected_data)

    def test_health_check_method_not_allowed(self):
        """
        Test if POST method on health check endpoint returns 405 Method Not Allowed.
        """
        response = self.client.post(self.url, {})
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )


class TestRegisterUserView(TestCase):
    """Test User can register to the application"""

    def setUp(self):
        self.client = APIClient()
        self.url = reverse("register")

    def test_registration_success(self):
        data = {
            "username": "test_user",
            "email": "test_user@example.com",
            "password": "test_password",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestTokenObtainView(TestCase):
    """Test login api return access token"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="test_user",
            email="test_user@example.com",
            password="test_password",
        )
        self.url = reverse("token_obtain_pair")

    def test_access_token_success(self):
        data = {"username": "test_user", "password": "test_password"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
