from rest_framework import serializers
from djstripe.models import Price, Subscription, PaymentMethod


class PriceSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Price
        fields = ['pk', 'id', 'metadata', 'active', 'currency',
                  'recurring', 'type', 'amount']

    def get_amount(self, instance):
        return instance.unit_amount / 100


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = '__all__'
