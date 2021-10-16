from rest_framework import serializers
from djstripe.models import Price


class PriceSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Price
        fields = ['id', 'metadata', 'active', 'currency',
                  'recurring', 'type', 'amount']

    def get_amount(self, instance):
        return instance.unit_amount / 100
