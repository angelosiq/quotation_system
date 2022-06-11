import pytest

from collections import defaultdict

from model_bakery import baker

from rest_framework.response import Response

from django.utils import timezone


ENDPOINT_CURRENCIES = "/api/currencies"
ENDPOINT_RATES = "/api/rates"

@pytest.mark.django_db
def test_api_currencies_without_credentials(api_client):
    """api currencies without credentials."""

    response = api_client.get(
        f"{ENDPOINT_CURRENCIES}/",
        format='json'
    )
    assert response.status_code == 200

@pytest.mark.django_db
def test_api_rates_without_credentials(api_client):
    """api rates without credentials."""

    response = api_client.get(
        f"{ENDPOINT_RATES}/",
        format='json'
    )
    assert response.status_code == 200

@pytest.mark.django_db
def test_api_currencies_check_list(api_client):
    """api rates check list."""

    baker.make('quotation.Currency', _quantity=10)

    response = api_client.get(
        f"{ENDPOINT_CURRENCIES}/",
        format='json'
    )
    assert len(response.data) == 10

@pytest.mark.django_db
def test_api_rate_charts(api_client, rate_instance):
    rate_instance.ratecurrency_set.add(*baker.make('RateCurrency', _quantity=10))
    
    data = rate_instance.ratecurrency_set.all().values_list('currency__code', 'rate__date', 'value')
    chart_data = defaultdict(list)
    for element in data:
        date = timezone.datetime.combine(element[1], timezone.datetime.min.time())
        date = timezone.datetime.timestamp(date)*1000
        chart_data[element[0]].append([date, element[2]])

    response_ = defaultdict(list)
    for currency, values_list in rate_instance.chart_rates.items():
        response_[currency].append(values_list[0])

    response = api_client.get(
        f"{ENDPOINT_RATES}/rate_chart/",
        format='json'
    )
    assert response.data == response_
