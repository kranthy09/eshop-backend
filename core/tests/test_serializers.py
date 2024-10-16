"""
Test Core App Serializers
"""

import pytest
from core.serializers import (
    UserSerializer,
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    VariantSerializer,
    SpecificationSerializer,
    CompatibilitySerializer,
    DeliveryTimeStatusSerializer,
    FaqSerializer,
    CarouselSerializer,
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
    """Test response model for Variant"""

    serializer = VariantSerializer(variant)
    data = serializer.data
    assert data["id"] == variant.id
    assert data["name"] == variant.name
    assert data["price"] == str(variant.price)
    assert data["color"] == variant.color
    assert data["stock"] == variant.stock
    assert data["size"] == variant.size
    assert data["product"]["base_name"] == variant.product.base_name


@pytest.mark.django_db
def test_specification_model_serializer(specification):
    """Test response model for Specification"""

    serializer = SpecificationSerializer(specification)
    data = serializer.data
    assert data["id"] == specification.id
    assert data["name"] == specification.name
    assert data["value"] == specification.value
    assert data["product"]["base_name"] == specification.product.base_name


@pytest.mark.django_db
def test_compatibility_model_serializer(compatibility):
    """Test response model for Compatibility"""

    serializer = CompatibilitySerializer(compatibility)
    data = serializer.data
    assert data["id"] == compatibility.id
    assert data["name"] == compatibility.name
    assert data["product_type"] == compatibility.product_type
    assert data["product"]["base_name"] == compatibility.product.base_name


@pytest.mark.django_db
def test_deliverytimestatus_model_serializer(deliverytimestatus):
    """Test response model for DeliveryTimeStatus"""

    serializer = DeliveryTimeStatusSerializer(deliverytimestatus)
    data = serializer.data
    assert data["id"] == deliverytimestatus.id
    assert data["shipping_cost"] == str(deliverytimestatus.shipping_cost)
    assert (
        data["estimated_delivery_time"]
        == deliverytimestatus.estimated_delivery_time
    )
    assert data["additional_info"] == deliverytimestatus.additional_info
    assert (
        data["product"]["base_name"] == deliverytimestatus.product.base_name
    )


@pytest.mark.django_db
def test_faq_model_serializer(faq):
    """Test response model for FAQ"""

    serializer = FaqSerializer(faq)
    data = serializer.data
    assert data["id"] == faq.id
    assert data["question"] == faq.question
    assert data["answer"] == faq.answer
    assert data["product"]["base_name"] == faq.product.base_name


@pytest.mark.django_db
def test_carousel_model_serializer(carousel):
    """Test response model for Carousel"""

    serializer = CarouselSerializer(carousel)
    data = serializer.data
    assert data["id"] == carousel.id
    assert data["image"] == carousel.image
    assert data["product"]["base_name"] == carousel.product.base_name
