"""Database models for Core App"""

import re
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model for Entire Application"""

    is_admin = models.BooleanField(default=False)


class Brand(models.Model):
    """Brand model for a set of Products"""

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.name}"


class Category(models.Model):
    """Category model for a set of Products"""

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.name}"


class Image(models.Model):
    """Image model"""

    url = models.URLField(max_length=999, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.url}"


class Product(models.Model):
    """Product Model"""

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        Brand, related_name="products", on_delete=models.CASCADE
    )
    base_name = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.base_name} | {self.category.name}"


class Variant(models.Model):
    """Product variants"""

    product = models.ForeignKey(
        Product, related_name="variants", on_delete=models.CASCADE
    )
    images = models.ManyToManyField(
        Image,
        null=True,
        related_name="variant_images",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    size = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sepcification(models.Model):
    """Product specifications"""

    product = models.ForeignKey(
        Variant, on_delete=models.CASCADE, related_name="specifications"
    )
    name = models.CharField(max=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Compatibility(models.Model):
    """Product compatibility"""

    product = models.ForeignKey(
        Product, related_name="compatibility", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DeliveryTimeStatus(models.Model):
    """Product delivery time status"""

    product = models.OneToOneField(
        Product, related_name="delivery_time_status", on_delete=models.CASCADE
    )
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_delivery_time = models.CharField(max_length=100)
    additional_info = models.TextField(max_length=True)


class Faq(models.Model):
    """Product FAQ"""

    product = models.ForeignKey(
        Product, related_name="faqs", on_delete=models.CASCADE
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.question}"


class Carousel(models.Model):
    """Product carousel images, description"""

    product = models.ForeignKey(
        Product, related_name="carousel", on_delete=models.CASCADE
    )
    image = models.URLField(max_length=999, null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.image}"


class Review(models.Model):
    """Product review"""

    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    images = models.ManyToManyField(
        Image, null=True, related_name="images", on_delete=models.CASCADE
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


class Cart(models.Model):
    """User Cart"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    """Cart Items"""

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items"
    )
    product_variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product_variant.name} x {self.quantity}"
