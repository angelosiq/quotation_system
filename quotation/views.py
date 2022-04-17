from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from quotation.models import Currency, Rate
from quotation.serializers import CurrencySerializer, RateSerializer


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)


class RateViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = (AllowAny,)
