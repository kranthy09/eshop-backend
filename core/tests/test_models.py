"""
Test cases for Core models
"""

import pytest
from core.models import User, Category, Brand


@pytest.mark.django_db
def test_user_model(user):
    """Test User model"""

    assert user.username == "test1"
    assert user.email == "test1@example.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    assert user.is_admin is False


@pytest.mark.django_db
def test_category_model(category):
    """Test category model"""

    assert category.name == "test_category"
    assert category.description == "test category description"


@pytest.mark.django_db
def test_brand_model(brand):
    """Test brand model"""

    assert brand.name == "test_brand"
    assert brand.description == "test brand description"


@pytest.mark.django_db
def test_product_model(product):
    """Test product model"""

    assert product.base_name == "test_product"
    assert product.description == "test product description"
    assert product.base_price == 10.99
    assert product.category.name == "test_category"
    assert product.brand.name == "test_brand"
