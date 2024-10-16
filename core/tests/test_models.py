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


@pytest.mark.django_db
def test_variant_model(variant):
    """Test variant model"""

    assert variant.product.base_name == "test_product"
    assert variant.name == "test_variant"
    assert variant.price == 5.99
    assert variant.color == "Black"
    assert variant.stock == 5
    assert variant.size == "M"


@pytest.mark.django_db
def test_specification_model(specification):
    """Test specification model"""

    assert specification.product.base_name == "test_product"
    assert specification.name == "material"
    assert specification.value == "Polymer"


@pytest.mark.django_db
def test_compatibility_model(compatibility):
    """Test compatibility model"""

    assert compatibility.product.base_name == "test_product"
    assert compatibility.name == "test_compatibility"
    assert compatibility.product_type == "Electronic"


@pytest.mark.django_db
def test_deliverytimestatus(deliverytimestatus):
    """Test deliverytimestatus model"""

    assert deliverytimestatus.product.base_name == "test_product"
    assert deliverytimestatus.shipping_cost == 1.99
    assert deliverytimestatus.estimated_delivery_time == "3-5 days"
    assert (
        deliverytimestatus.additional_info == "Additional delivery information"
    )


@pytest.mark.django_db
def test_faq_model(faq):
    """Test faq model"""

    assert faq.product.base_name == "test_product"
    assert faq.question == "Test FAQ question"
    assert faq.answer == "Test FAQ answer"


@pytest.mark.django_db
def test_carousel_model(carousel):
    """Test carousel model"""

    assert carousel.product.base_name == "test_product"
    assert carousel.image == "test_carousel_image"
    assert carousel.title == "Test carousel caption"
    assert carousel.description == "Test carousel description"
    assert carousel.order == 1
