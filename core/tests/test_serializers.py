"""
Test Core App Serializers
"""

import pytest
from core.serializers import (
    UserSerializer,
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
)


@pytest.mark.django_db
def test_user_model_serializer(user):
    """Test User Model Serializer."""
    serializer = UserSerializer(user)
    assert serializer.data == {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "is_admin": user.is_admin,
    }


@pytest.mark.django_db
def test_brand_model_serializer(brand):
    """Test response model for Brand"""

    serializer = BrandSerializer(brand)
    data = serializer.data
    assert data["id"] == brand.id
    assert data["name"] == brand.name
    assert data["description"] == brand.description


@pytest.mark.django_db
def test_category_model_serializer(category):
    """Test Response model for Category"""
    serializer = CategorySerializer(category)
    data = serializer.data
    assert data["id"] == category.id
    assert data["name"] == category.name
    assert data["description"] == category.description


@pytest.mark.django_db
def test_product_model_serializer(product):
    """Test Response model for Product"""

    serializer = ProductSerializer(product)
    data = serializer.data
    assert data["id"] == product.id
    assert data["base_name"] == product.base_name
    assert data["description"] == product.description
    assert data["base_price"] == str(product.base_price)
    assert data["brand"]["id"] == product.brand.id
    assert data["brand"]["name"] == product.brand.name
    assert data["category"]["id"] == product.category.id
    assert data["category"]["name"] == product.category.name


@pytest.mark.django_db
def test_variant_model_serializer(variant):
    pass
