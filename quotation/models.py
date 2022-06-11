from collections import defaultdict

from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _


class Currency(models.Model):
    """Model definition for Currency."""

    code = models.CharField(_('Código'), max_length=255)
    name = models.CharField(_('Nome'), max_length=255)
    symbol = models.CharField(_('Símbolo'), max_length=255)

    class Meta:
        """Meta definition for Currency."""
        verbose_name = _('Moeda')
        verbose_name_plural = _('Moedas')

    def __str__(self):
        return self.code


class Rate(models.Model):
    """Model definition for Rate."""

    date = models.DateField(_('Data'))
    base_currency = models.ForeignKey(
        'quotation.Currency', related_name="base_currency", on_delete=models.CASCADE, verbose_name=_('Moeda base'))
    rate = models.ManyToManyField(
        'quotation.Currency',
        through='quotation.RateCurrency',
        verbose_name=_('Proporção da moeda'),
        related_name='rate_list',
        blank=True
    )

    class Meta:
        """Meta definition for Rate."""

        verbose_name = _('Proporção')
        verbose_name_plural = _('Proporções')

    def __str__(self):
        return f"{self.base_currency.code} - {self.date.strftime('%Y-%m-%d')}"

    @cached_property
    def chart_rates(self):
        def date_to_timestamp_unix_format(date):
            return (
                datetime_format := timezone.datetime.combine(date, timezone.datetime.min.time())
            ) and int(timezone.datetime.timestamp(datetime_format)*1000)

        rate_data = self.ratecurrency_set.all().order_by('-rate__date').values_list(
                'currency__code', 'rate__date', 'value')
        chart_data = defaultdict(list)

        for currency_code, rate_date, value in rate_data:
            chart_data[currency_code].append([date_to_timestamp_unix_format(rate_date), value])
            
        return chart_data

    @staticmethod
    def chart_formatted_data():
        formatted_data = defaultdict(list)
        rates = Rate.objects.all()

        if rates:
            for rate in rates:
                for currency, values_list in rate.chart_rates.items():
                    formatted_data[currency].append(values_list[0])

        return formatted_data


class RateCurrency(models.Model):
    """Model definition for RateCurrency."""

    value = models.DecimalField(
        _('Valor'),
        max_digits=10,
        decimal_places=2
    )
    currency = models.ForeignKey('quotation.Currency', on_delete=models.CASCADE, verbose_name=_('Moeda'))
    rate = models.ForeignKey('quotation.Rate', on_delete=models.CASCADE, verbose_name=_('Proporção'))

    class Meta:
        """Meta definition for RateCurrency."""

        verbose_name = _('Proporção da moeda')
        verbose_name_plural = _('Proporções das moedas')
