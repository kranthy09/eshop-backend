from django.contrib import admin
from core.models import (
    User,
    Category,
    Brand,
    Image,
    Product,
    Variant,
    Specification,
    Compatibility,
    DeliveryTimeStatus,
    Faq,
    Carousel,
)

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Specification)
admin.site.register(Compatibility)
admin.site.register(DeliveryTimeStatus)
admin.site.register(Faq)
admin.site.register(Carousel)
admin.site.register(Image)
