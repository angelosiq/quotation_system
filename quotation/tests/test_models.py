import pytest

from collections import defaultdict

from model_bakery import baker

from django.utils import timezone


@pytest.mark.django_db
def test_currency_str():
    code = 'test'
    currency = baker.make('quotation.Currency', code=code)
    assert str(currency) == code


@pytest.mark.django_db
def test_rate_str(currency_instance):
    rate = baker.make('quotation.Rate', base_currency=currency_instance)
    assert str(rate) == f"{currency_instance.code} - {rate.date.strftime('%Y-%m-%d')}"


@pytest.mark.django_db
def test_rate_chart_rates(rate_instance):
    rate_instance.ratecurrency_set.add(*baker.make('RateCurrency', _quantity=10))
    
    data = rate_instance.ratecurrency_set.all().values_list('currency__code', 'rate__date', 'value')
    chart_data = defaultdict(list)
    for element in data:
        date = timezone.datetime.combine(element[1], timezone.datetime.min.time())
        date = timezone.datetime.timestamp(date)*1000
        chart_data[element[0]].append([date, element[2]])

    assert rate_instance.chart_rates == chart_data
