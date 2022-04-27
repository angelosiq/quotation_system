from collections import defaultdict
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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

    @action(methods=['get'], detail=False)
    def rate_chart(self, request):
        response = defaultdict(list)
        rate = Rate.objects.all()

        if rate:
            for r in rate:
                for currency, values_list in r.chart_rates.items():
                    response[currency].append(values_list[0])
        else:
            return Response("Nada encontrado.", status=status.HTTP_200_OK)

        return Response(response, status=status.HTTP_200_OK)
