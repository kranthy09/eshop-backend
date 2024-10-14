"""
Test Review API, GET POST PUT DELETE PATCH
"""

from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from core.models import User, Product, Category, Brand, Tags


class TestTagsAPI(TestCase):
    """Test Review API"""

    def setUp(self):
        """Set up the variables and databases"""
        self.client = APIClient()
        self.url = reverse("tags-list")
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

    def create_category(self):
        """Create a new category"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        return category

    def create_brand(self):
        """Create a new brand"""
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
        return brand

    def create_product(self, category, brand):
        """Create a new product"""
        product_data = {
            "name": "test_product",
            "image_url": "https://cdn.pixabay.com/photo/2014/06/03/19/38/board-361516_640.jpg",
            "description": "test product description",
            "price": 10.99,
            "stock": 5,
            "rating": 4,
            "metadata": {
                "product_details": {
                    "brand": "KeyMaster",
                    "model": "KM-202",
                    "color": "Black",
                    "warranty": "1 year",
                },
                "specifications": {
                    "key_switch_type": "Cherry MX Red",
                    "backlighting": "RGB",
                    "connectivity": "USB",
                },
            },
            "category": category,
            "brand": brand,
        }
        return Product.objects.create(**product_data)

    def create_category(self):
        """Create a new category"""
        category = Category.objects.create(
            name="test category",
            description="test category description",
        )
        return category

    def test_create_tag(self):
        """Test creating a new review."""
        brand = self.create_brand()
        category = self.create_category()
        product = self.create_product(category, brand)
        tag_data = {
            "tag_name": "test_tag",
            "product": product.id,
        }
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.post(
            self.url, data=tag_data, format="json", headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Tags.objects.get().tag_name, response.data.get("tag_name")
        )

    def test_get_tags(self):
        """Test review list"""
        category = self.create_category()
        brand = self.create_brand()
        product = self.create_product(category, brand)
        Tags.objects.create(
            tag_name="test_tag",
            product=product,
        )
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            Tags.objects.get().tag_name, response.data[0]["tag_name"]
        )

    def test_tag_detail(self):
        """Test review detail."""
        brand = self.create_brand()
        category = self.create_category()
        product = self.create_product(category, brand)
        tag = Tags.objects.create(
            tag_name="test_tag",
            product=product,
        )
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.get(
            reverse("tags-detail", kwargs={"pk": tag.id}), headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Tags.objects.get().tag_name, response.data["tag_name"]
        )

    def test_patch_tag(self):
        """Test updating review."""
        brand = self.create_brand()
        category = self.create_category()
        product = self.create_product(category, brand)
        tag = Tags.objects.create(
            tag_name="test_tag",
            product=product,
        )
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.patch(
            reverse("tags-detail", kwargs={"pk": tag.id}),
            data={"tag_name": "updated tag name"},
            format="json",
            headers=headers,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tags.objects.get().tag_name, "updated tag name")

    def test_delete_tag(self):
        """Test deleting review."""
        brand = self.create_brand()
        category = self.create_category()
        product = self.create_product(category, brand)
        tag = Tags.objects.create(
            tag_name="test_tag",
            product=product,
        )
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.delete(
            reverse("tags-detail", kwargs={"pk": tag.id}), headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tags.objects.count(), 0)
