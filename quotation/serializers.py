from rest_framework import serializers

from quotation.models import Currency, Rate, RateCurrency


class CurrencySerializer(serializers.ModelSerializer):
    """Serializer for Currency model."""

    class Meta:
        """Meta for Currency model serializer."""

        model = Currency
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    """Serializer for Rate model."""

    class Meta:
        """Meta for Rate model serializer."""

        model = Rate
        fields = '__all__'


class RateCurrencySerializer(serializers.ModelSerializer):
    """Serializer for RateCurrency model."""

    class Meta:
        """Meta for RateCurrency model serializer."""

        model = RateCurrency
        fields = '__all__'
