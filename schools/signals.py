import stripe
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

from schools.models import School


@receiver(post_delete, sender=School)
def cancel_subscription_on_delete(sender, instance, **kwargs):
    """ Cancel subscription on school delete """

    if instance.subscription is not None:
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        sub_id = instance.subscription.id
        stripe.Subscription.delete(sub_id)
        instance.subscription.delete()
