from django.db import models
from django.utils.translation import gettext_lazy as _


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


class RateCurrency(models.Model):
    """Model definition for RateCurrency."""

    value = models.FloatField(_('Valor'))
    currency = models.ForeignKey('quotation.Currency', on_delete=models.CASCADE, verbose_name=_('Moeda'))
    rate = models.ForeignKey('quotation.Rate', on_delete=models.CASCADE, verbose_name=_('Proporção'))

    class Meta:
        """Meta definition for RateCurrency."""

        verbose_name = _('Proporção da moeda')
        verbose_name_plural = _('Proporções das moedas')