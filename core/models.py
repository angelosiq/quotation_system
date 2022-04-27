from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


BLANK_NULL = {'blank': True, 'null': True}


class Settings(SingletonModel):
    """Model definition for QuotationSystem Settings"""

    quotation_api = models.CharField(max_length=255, **BLANK_NULL)

    class Meta:
        """Meta definition for Settings."""
        verbose_name = _('Configurações do sistema')

    def __str__(self):
        return f'{self._meta.verbose_name}'
