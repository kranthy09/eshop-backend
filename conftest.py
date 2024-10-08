"""
Database fixtures and API Client rquests
"""

import pytest
from rest_framework.test import APIClient
from core.models import User, Brand, Category, Product


@pytest.fixture
def api_client():
    """
    Initialize and return client instance to make requests to endpoints
    """
    return APIClient()


@pytest.fixture
def user():
    """Create and return user instance"""
    return User.objects.create(
        username="test1",
        email="test1@example.com",
        password="passwordmadeeasy",
    )


@pytest.fixture
def category():
    """create and return category instance"""
    return Category.objects.create(
        name="test_category", description="test category description"
    )


@pytest.fixture
def brand():
    """create and return brand instance"""

    return Brand.objects.create(
        name="test_brand",
        description="test brand description",
    )


@pytest.fixture
def product(category, brand):
    """create and return product instance"""

    return Product.objects.create(
        name="test_product",
        description="test product description",
        price=10.99,
        category=category,
        brand=brand,
        image_url="https://image_url.com",
        stock=5,
        rating=4,
        metadata={
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
    )


@pytest.fixture
def review(user, product):
    """create and return review instance"""

    return product.reviews.create(
        reviewer=user,
        product=product,
        comment="Test review comment",
        rating=5,
    )


@pytest.fixture
def tag(product):
    """create and return tag instance"""

    return product.tags.create(tag_name="test_tag")
