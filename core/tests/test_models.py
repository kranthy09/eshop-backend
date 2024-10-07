"""
Test cases for Core models
"""

import pytest
from core.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        username="test_user",
        email="test_user@example.com",
        password="test_password",
    )

    assert user.username == "test_user"
    assert user.email == "test_user@example.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    assert user.is_admin is False
