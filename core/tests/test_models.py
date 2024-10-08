"""
Test cases for Core models
"""

import pytest
from core.models import User, Category, Brand, Product


@pytest.mark.django_db
def test_create_user():
    """Test User model"""
    user = User.objects.create_user(
        username="test_user",
        email="test_user@example.com",
        password="test_password",
    )

    assert user.username == "test_user"
    assert user.email == "test_user@example.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    assert user.is_admin is False


@pytest.mark.django_db
def test_category_model():
    """Test category model"""
    category = Category.objects.create(
        name="test_category", description="test category description"
    )

    assert category.name == "test_category"
    assert category.description == "test category description"


@pytest.mark.django_db
def test_brand_model():
    """Test brand model"""
    brand = Brand.objects.create(
        name="test_brand", description="test brand description"
    )

    assert brand.name == "test_brand"
    assert brand.description == "test brand description"


@pytest.mark.django_db
def test_product_model(product):
    """Test product model"""

    assert product.name == "test_product"
    assert product.image_url == "https://image_url.com"
    assert product.description == "test product description"
    assert product.price == 10.99
    assert product.stock == 5
    assert product.rating == 4
    assert product.metadata["product_details"] == {
        "brand": "KeyMaster",
        "model": "KM-202",
        "color": "Black",
        "warranty": "1 year",
    }


@pytest.mark.django_db
def test_review_model(review):
    """Test review model"""

    assert review.comment == "Test review comment"
    assert review.rating == 5
    assert review.product.name == "test_product"


@pytest.mark.django_db
def test_tag_model(tag):
    """Test tag model"""

    assert tag.tag_name == "test_tag"
    assert tag.product.name == "test_product"
