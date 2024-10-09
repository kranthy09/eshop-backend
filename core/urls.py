"""
URL enpoints to core App
"""

from django.urls import path
from core.views import (
    HealthCheckView,
    RegisterUserView,
    ProfileView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    BrandListAPIView,
    BrandDetailAPIView,
    BrandPartialUpdateAPIView,
)


urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health-check"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="user-profile"),
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path(
        "category-detail/<int:pk>",
        CategoryDetailAPIView.as_view(),
        name="category-detail",
    ),
    path("brands/", BrandListAPIView.as_view(), name="brand-list"),
    path(
        "brand-detail/<int:pk>",
        BrandDetailAPIView.as_view(),
        name="brand-detail",
    ),
    path(
        "brand-partial-update/<int:pk>",
        BrandPartialUpdateAPIView.as_view(),
        name="partial-update-brand",
    ),
]
