import datetime

import requests

from django.utils.translation import ugettext_lazy as _

from core.models import Settings

from quotation.models import Currency, Rate, RateCurrency


VALID_CURRENCIES = ["EUR", "USD", "JPY", "BRL"]


def get_currencies():
    settings = Settings.get_solo()
    if settings.quotation_api:
        currencies = requests.get(url=f"{settings.quotation_api}currencies").json()
    else:
        raise Exception(_('API inválida.'))
    currency_list = []
    for code, data in currencies.items():
        if code in VALID_CURRENCIES:
            currency_instance = Currency.objects.get_or_create(
                code=code, name=data.get('name'), symbol=data.get('symbol'))[0]
            currency_list.append(currency_instance)

    return currency_list


def get_rates():
    settings = Settings.get_solo()
    date = datetime.date.today()
    count_days = 0
    base_currency = Currency.objects.get_or_create(code="USD")[0]
    rates_list = []

    while count_days < 5:
        date_string = date.strftime('%Y-%m-%d')
        if settings.quotation_api:
            rates_response = requests.get(
                url=f"{settings.quotation_api}rates?base={base_currency.code}&date={date_string}").json()
        else:
            raise Exception(_('API inválida.'))

        if date_string == rates_response.get('date'):
            rate = Rate.objects.get_or_create(date=date, base_currency=base_currency)[0]
            for currency, value in rates_response.get('rates').items():
                if currency in VALID_CURRENCIES and currency != base_currency.code:
                    currency_instance = Currency.objects.get(code=currency)
                    rate_currency = RateCurrency.objects.create(value=value, rate=rate, currency=currency_instance)
                    rate.ratecurrency_set.add(rate_currency)

            rates_list.append(rate)
            count_days += 1

        date = date - datetime.timedelta(days=1)

    return rates_list


def get_data():
    currencies = Currency.objects.all()
    currencies.delete()

    currencies = get_currencies()
    rates = get_rates()

    return {
        "currencies": currencies,
        "rates": rates
    }
