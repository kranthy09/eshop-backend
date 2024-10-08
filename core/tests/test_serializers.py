"""
Test Core App Serializers
"""

import pytest
from core.serializers import (
    UserSerializer,
    ProductSerializer,
    CategorySerializer,
    BrandSerializer,
    ReviewSerilizer,
    TagsSerializer,
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
def test_product_model_serializer(product):
    """Test Reponse model for Product"""

    serializer = ProductSerializer(product)
    data = serializer.data
    assert data["id"] == product.id
    assert data["name"] == product.name
    assert data["description"] == product.description
    assert data["price"] == str(product.price)


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
def test_review_model_serializer(review):
    """Test Response model for review"""

    serializer = ReviewSerilizer(review)
    data = serializer.data
    assert data["id"] == review.id
    assert data["reviewer"] == review.reviewer.id
    assert data["product"] == review.product.id
    assert data["comment"] == review.comment
    assert data["rating"] == review.rating


@pytest.mark.django_db
def test_tags_model_serializer(tag):
    """Test Response model for tags"""

    serializer = TagsSerializer(tag)
    data = serializer.data
    assert data["id"] == tag.id
    assert data["product"] == tag.product.id
    assert data["tag_name"] == tag.tag_name
