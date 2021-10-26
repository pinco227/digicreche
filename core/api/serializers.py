from djstripe.models import PaymentMethod, Plan, Subscription
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ['djstripe_id', 'id', 'metadata', 'active', 'currency',
                  'interval', 'interval_count', 'amount']


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = '__all__'
