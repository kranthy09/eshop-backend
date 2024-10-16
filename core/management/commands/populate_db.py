"""
populate database models with data
"""

from django.db import transaction
from django.core.management.base import BaseCommand
from core.models import (
    Category,
    Brand,
    Product,
    Variant,
    Specification,
    Compatibility,
    DeliveryTimeStatus,
    Faq,
    Carousel,
)


class Command(BaseCommand):
    """Custom command to populate db models"""

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """command handler method"""
        # category
        category = Category.objects.create(
            name="Table Organizers", description="Organize things on table"
        )
        # brand
        brand = Brand.objects.create(
            name="Leatherwood", description="Leatherwood brand of furniture"
        )
        # product
        product = Product.objects.create(
            base_name="Leatherwood Table",
            description="Leatherwood table with built-in storage",
            base_price=159.99,
            category=category,
            brand=brand,
        )
        # variant
        Variant.objects.create(
            product=product,
            name="Black",
            price=139.99,
            color="Black",
            stock=10,
            size="M",
        )
        Variant.objects.create(
            product=product,
            name="White",
            price=139.99,
            color="White",
            stock=5,
            size="L",
        )
        # specification
        Specification.objects.create(
            product=product, name="Material", value="Polymer"
        )
        Specification.objects.create(
            product=product, name="Color", value="Black"
        )
        Specification.objects.create(
            product=product, name="Weight", value="150g"
        )
        Compatibility.objects.create(
            product=product,
            name="Leatherwood",
            product_type="Table",
        )
        Compatibility.objects.create(
            product=product,
            name="Leatherwood",
            product_type="Chair",
        )
        DeliveryTimeStatus.objects.create(
            product=product,
            shipping_cost=2.99,
            estimated_delivery_time="3-5 days",
            additional_info="Standard shipping",
        )
        Faq.objects.create(
            product=product,
            question="How to clean Leatherwood Table?",
            answer="Clean it with soft soap and water",
        )
        Faq.objects.create(
            product=product,
            question="What is the warranty period?",
            answer="Warranty period is 1 year",
        )
        Carousel.objects.create(
            product=product,
            image="https://image_url.com/leatherwood_table.jpg",
            title="Leatherwood Table",
            description="Leatherwood table at the best price",
            order=1,
        )
        Carousel.objects.create(
            product=product,
            image="https://image_url.com/leatherwood_table_2.jpg",
            title="Leatherwood Table 2",
            description="Leatherwood table with built-in storage",
            order=2,
        )

        self.stdout.write(
            self.style.SUCCESS("Database populated successfully")
        )
