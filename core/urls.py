"""
URL enpoints to core App
"""

from django.urls import path
from core.views import HealthCheckView, RegisterUserView, TokenObtainView

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health-check"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", TokenObtainView.as_view(), name="login"),
]
