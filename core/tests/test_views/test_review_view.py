"""
Test Review API, GET POST PUT DELETE PATCH
"""

from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from core.models import User, Review, Product, Category, Brand


class TestReviewAPI(TestCase):
    """Test Review API"""

    def setUp(self):
        """Set up the variables and databases"""
        self.client = APIClient()
        self.url = reverse("review-list")
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

    def test_create_review(self):
        """Test creating a new review."""
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

        post_data = {
            "rating": 5,
            "comment": "test review comment",
            "reviewer": self.user.id,
            "product": product.id,
        }
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.post(
            self.url, data=post_data, format="json", headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Review.objects.get().rating, response.data.get("rating")
        )

    def test_get_reviews(self):
        """Test review list"""
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

        Review.objects.create(
            rating=5,
            comment="test review comment",
            reviewer=self.user,
            product=product,
        )
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            Review.objects.get().rating, response.data[0]["rating"]
        )

    def test_review_detail(self):
        """Test review detail."""
        brand = self.create_brand()
        category = self.create_category()
        product = self.create_product(category, brand)
        review = Review.objects.create(
            rating=5,
            comment="test review comment",
            reviewer=self.user,
            product=product,
        )
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.get(
            reverse("review-detail", kwargs={"pk": review.id}), headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.get().rating, response.data["rating"])

    def test_patch_review(self):
        """Test updating review."""
        brand = self.create_brand()
        category = self.create_category()
        product = self.create_product(category, brand)
        review = Review.objects.create(
            rating=5,
            comment="test review comment",
            reviewer=self.user,
            product=product,
        )
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.patch(
            reverse("review-detail", kwargs={"pk": review.id}),
            data={"rating": 4},
            format="json",
            headers=headers,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.get().rating, 4)

    def test_delete_review(self):
        """Test deleting review."""
        brand = self.create_brand()
        category = self.create_category()
        product = self.create_product(category, brand)
        review = Review.objects.create(
            rating=5,
            comment="test review comment",
            reviewer=self.user,
            product=product,
        )
        headers = {"Authorization": "Bearer " + self.access_token}
        response = self.client.delete(
            reverse("review-detail", kwargs={"pk": review.id}), headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0)
