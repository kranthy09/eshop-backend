"""
Test Product API, GET POST PUT PATCH DELETE
"""

import json
import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import User, Category, Product, Brand
from core.serializers import ProductSerializer


class TestProductAPI(TestCase):
    """Test Product API"""

    def setUp(self):
        """Set up variables and database"""
        self.client = APIClient()
        self.url = reverse("product-list")
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

    def test_create_product(self):
        """Test creating a new product"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
        post_data = {
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
            "category": category.id,
            "brand": brand.id,
        }
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.post(
            self.url, data=post_data, format="json", headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.get().name, response.data.get("name"))
        self.assertEqual(
            Product.objects.get().metadata, response.data.get("metadata")
        )

    def test_get_products(self):
        """Test creating a new product"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
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
        product = Product.objects.create(**product_data)
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(Product.objects.get().name, response.data[0]["name"])
        self.assertEqual(
            Product.objects.get().metadata, response.data[0]["metadata"]
        )

    def test_product_detail(self):
        """Test creating a new product"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
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
        product = Product.objects.create(**product_data)
        self.url = reverse("product-detail", args=[product.id])
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().name, response.data.get("name"))
        self.assertEqual(
            Product.objects.get().metadata, response.data.get("metadata")
        )

    def test_product_update(self):
        """Test creating a new product"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
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
        product = Product.objects.create(**product_data)
        self.url = reverse("product-detail", args=[product.id])
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.patch(
            self.url, data={"name": "updated name product"}, headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("updated name product", response.data.get("name"))
        self.assertEqual(
            Product.objects.get().metadata, response.data.get("metadata")
        )

    def test_product_delete(self):
        """Test creating a new product"""
        category = Category.objects.create(
            name="test_category", description="test category description"
        )
        brand = Brand.objects.create(
            name="test_brand", description="test brand description"
        )
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
        product = Product.objects.create(**product_data)
        self.url = reverse("product-detail", args=[product.id])
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.delete(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
