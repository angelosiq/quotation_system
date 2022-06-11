from model_bakery import baker

from django.test import TestCase


class CurrencyModelTestCase(TestCase):
    def setUp(self):
        self.currency_code = "test"
        self.currency = baker.make("quotation.Currency", code=self.currency_code)

    def test_currency_str(self):
        self.assertEquals(self.currency.code, self.currency_code)


class RateModelTestCase(TestCase):
    def setUp(self):
        self.currency = baker.make("quotation.Currency")
        self.rate = baker.make("quotation.Rate")

    def test_rate_str(self):
        self.rate.base_currency = self.currency
        self.rate.save()
        self.assertEquals(str(self.rate), f"{self.currency.code} - {self.rate.date.strftime('%Y-%m-%d')}")

    @staticmethod
    def create_rate_currencies_by_currency_code(currency_code, rate_currencies_quantity):
        currency = baker.make("quotation.Currency", code=currency_code)
        rate_currencies = baker.make('quotation.RateCurrency', currency=currency, _quantity=rate_currencies_quantity)
        return rate_currencies

    def test_rate_chart_rates(self):
        currency_eur_code = "EUR"

        self.rate.ratecurrency_set.add(
            *RateModelTestCase.create_rate_currencies_by_currency_code(currency_eur_code, 4))

        chart_rates = self.rate.chart_rates[currency_eur_code]
        self.assertEquals(len(chart_rates), 4)
        self.assertEquals(isinstance(chart_rates[0], list), True)
