"""
Test Category and Brand API
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import User, Category, Brand


class TestCategoryAPI(TestCase):
    """Test category"""

    def setUp(self):
        """Set up variables and database"""
        self.client = APIClient()
        self.url = reverse("category-list")
        self.user = User.objects.create_user(
            username="test_user",
            email="test_user@example.com",
            password="test_password",
        )
        response = self.client.post(
            reverse("token_obtain_pair"),
            data={
                "username": self.user.username,
                "password": "test_password",
            },
        )
        self.access_token = response.json()["access"]

    def test_create_category(self):
        """Test creating a category"""
        headers = {"Authorization": "Bearer " + self.access_token}
        data = {
            "name": "test_category",
            "description": "test category description",
        }
        response = self.client.post(self.url, data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category(self):
        """Test detail view for category"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        self.url = reverse("category-detail", args=[category.id])
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("name", response.data)
        self.assertEqual(response.data["name"], "test_category")

    def test_update_category(self):
        """Test updating category"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        self.url = reverse("category-detail", args=[category.id])
        updated_category = {
            "name": "updated_test_category",
            "description": "updated test category description",
        }
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.put(
            self.url, data=updated_category, headers=headers
        )
        assert response.status_code == 200
        self.assertIn("name", response.data)
        self.assertEqual(response.data["name"], "updated_test_category")
        self.assertEqual(
            response.data["description"], "updated test category description"
        )

    def test_delete_category(self):
        """Test Delete a category"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        self.url = reverse("category-detail", args=[category.id])
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.delete(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Category.objects.filter(pk=category.id).exists(), False
        )


class TestBrandCategory(TestCase):
    """Test brand and category"""

    def setUp(self):
        """Set up variables and database"""
        self.client = APIClient()
        self.url = reverse("brand-list")
        self.user = User.objects.create_user(
            username="test_user",
            email="test_user@example.com",
            password="test_password",
        )
        response = self.client.post(
            reverse("token_obtain_pair"),
            data={
                "username": self.user.username,
                "password": "test_password",
            },
        )
        self.access_token = response.json()["access"]

    def test_create_brand(self):
        """Test creating a brand"""
        headers = {"Authorization": "Bearer " + self.access_token}
        data = {
            "name": "test_brand",
            "description": "test brand description",
        }
        response = self.client.post(self.url, data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category(self):
        """Test detail view for brand"""
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
        self.url = reverse("brand-detail", args=[brand.id])
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("name", response.data)
        self.assertEqual(response.data["name"], "test_brand")

    def test_put_brand(self):
        """Test updating brand"""
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
        self.url = reverse("brand-detail", args=[brand.id])
        updated_brand = {
            "name": "updated_test_brand",
            "description": "updated test brand description",
        }
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.put(
            self.url, data=updated_brand, headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        self.assertIn("name", response.data)
        self.assertEqual(response.data["name"], "updated_test_brand")
        self.assertEqual(
            response.data["description"], "updated test brand description"
        )

    def test_patch_brand(self):
        """Test partial update brand"""

        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
        self.url = reverse("partial-update-brand", args=[brand.id])
        updated_brand = {"name": "updated_test_brand"}
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.put(
            self.url, data=updated_brand, headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("name", response.data)
        self.assertEqual(response.data["name"], "updated_test_brand")
        self.assertEqual(
            response.data["description"], "test brand description"
        )

    def test_delete_brand(self):
        """Test deleting a brand"""
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
        self.url = reverse("brand-detail", args=[brand.id])
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.delete(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brand.objects.filter(pk=brand.id).exists(), False)
