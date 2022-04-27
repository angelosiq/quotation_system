import pytest

from rest_framework.test import APIClient

from model_bakery import baker


@pytest.fixture
def api_client():
    """DRF client."""
    return APIClient()


@pytest.fixture
@pytest.mark.django_db
def currency_instance():
    return baker.make('quotation.Currency')


@pytest.fixture
@pytest.mark.django_db
def rate_instance():
    return baker.make('quotation.Rate')
