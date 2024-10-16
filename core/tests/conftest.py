"""
Database fixtures and API Client rquests
"""

import pytest

from rest_framework.test import APIClient
from core.models import (
    User,
    Brand,
    Category,
    Product,
    Variant,
    Specification,
    Compatibility,
    DeliveryTimeStatus,
    Faq,
    Carousel,
)


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


@pytest.fixture
def specification(product):
    """create and return specification instance"""

    return Specification.objects.create(
        product=product,
        name="material",
        value="Polymer",
    )


@pytest.fixture
def compatibility(product):
    """create and return compatibility instance"""

    return Compatibility.objects.create(
        product=product,
        name="test_compatibility",
        product_type="Electronic",
    )


@pytest.fixture
def deliverytimestatus(product):
    """create and return deliverytimestatus instance"""

    return DeliveryTimeStatus.objects.create(
        product=product,
        shipping_cost=1.99,
        estimated_delivery_time="3-5 days",
        additional_info="Additional delivery information",
    )


@pytest.fixture
def faq(product):
    """create and return faq instance"""

    return Faq.objects.create(
        product=product,
        question="Test FAQ question",
        answer="Test FAQ answer",
    )


@pytest.fixture
def carousel(product):
    """create and return Carousel instance"""

    return Carousel.objects.create(
        product=product,
        image="test_carousel_image",
        title="Test carousel caption",
        description="Test carousel description",
        order=1,
    )


# product-detail view, create product


@pytest.fixture
def product_detail_obj(product):
    """Create a product detail"""
    variant_objs = Variant.objects.bulk_create(
        [
            Variant(
                product=product,
                name="Black",
                price=5.99,
                color="Black",
                stock=5,
                size="M",
            ),
            Variant(
                product=product,
                name="Red",
                price=7.99,
                color="Red",
                stock=3,
                size="S",
            ),
        ]
    )
    sepcification_objs = Specification.objects.bulk_create(
        [
            Specification(product=product, name="Material", value="Polymer"),
            Specification(product=product, name="Color", value="Black"),
            Specification(product=product, name="Weight", value="150g"),
        ]
    )
    compatibility_objs = Compatibility.objects.bulk_create(
        [
            Compatibility(
                product=product, name="Electronic", product_type="Mobile"
            ),
            Compatibility(
                product=product, name="Electronic", product_type="Laptop"
            ),
        ]
    )
    delivery_time_status_obj = DeliveryTimeStatus.objects.create(
        product=product,
        shipping_cost=1.99,
        estimated_delivery_time="3-5 days",
        additional_info="Additional delivery information",
    )
    faq_objs = Faq.objects.bulk_create(
        [
            Faq(
                product=product,
                question="Test FAQ question",
                answer="Test FAQ answer",
            ),
            Faq(
                product=product,
                question="Test FAQ question 2",
                answer="Test FAQ answer 2",
            ),
            Faq(
                product=product,
                question="Test FAQ question 3",
                answer="Test FAQ answer 3",
            ),
        ]
    )
    carousel_objs = Carousel.objects.bulk_create(
        [
            Carousel(
                product=product,
                image="test_carousel_image1",
                title="Test carousel caption 1",
                description="Test carousel description 1",
                order=1,
            ),
            Carousel(
                product=product,
                image="test_carousel_image2",
                title="Test carousel caption 2",
                description="Test carousel description 2",
            ),
            Carousel(
                product=product,
                image="test_carousel_image3",
                title="Test carousel caption 3",
                description="Test carousel description 3",
            ),
        ]
    )

    return product
