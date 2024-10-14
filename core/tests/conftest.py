"""
Database fixtures and API Client rquests
"""

import pytest
from rest_framework.test import APIClient
from core.models import User, Brand, Category, Product, Variant


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
        base_name="test_product",
        description="test product description",
        base_price=10.99,
        category=category,
        brand=brand,
    )


@pytest.fixture
def variant(product):
    """create and return variant instance"""

    return Variant.objects.create(
        product=product,
        name="test_variant",
        price=5.99,
        color="Black",
        stock=5,
        size="M",
    )
