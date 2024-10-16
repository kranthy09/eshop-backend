"""
Test Product API, GET /product/{id}
"""

import logging
import pytest
from django.urls import reverse
from rest_framework import status

logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_get_product_detail(api_client, product_detail_obj):
    """Test GET /product/{id} endpoint"""

    url = reverse("product-detail", kwargs={"pk": product_detail_obj.id})
    response = api_client.get(url)
    response_json = response.json()
    logger.info("response given")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["base_name"] == product_detail_obj.base_name
    assert response.data["description"] == product_detail_obj.description
    assert response.data["base_price"] == str(product_detail_obj.base_price)
    assert (
        response.data["variants"][0]["name"]
        == product_detail_obj.variants.first().name
    )
