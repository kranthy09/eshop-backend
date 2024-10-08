"""Database models for Core App"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model for Entire Application"""

    is_admin = models.BooleanField(default=False)


class Category(models.Model):
    """Category model for a set of Products"""

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.name}"


class Brand(models.Model):
    """Brand model for a set of Products"""

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.name}"


class Product(models.Model):
    """Product Model"""

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand, null=True, related_name="brands", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(default=dict)

    def __str__(self) -> str:
        return f"{self.name} | {self.category.name}"


class Review(models.Model):
    """Product review"""

    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    comment = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.reviewer}"


class Tags(models.Model):
    """Product tags"""

    product = models.ForeignKey(
        Product, related_name="tags", on_delete=models.CASCADE
    )
    tag_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.tag_name}"
