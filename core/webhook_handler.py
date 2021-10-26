import djstripe.models as sm
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from schools.models import School


class StripeWH_Handler:
    """Handle Stripe webhooks."""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        print(f'Unhandled webhook received: {event["type"]}')
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_customer_created(self, event):
        """ Handle the payment_method.attached webhook event from Stripe"""
        print(f'Webhook received: {event["type"]}')

        customer = event.data.object
        user = get_object_or_404(get_user_model(), email=customer.email)

        # Checks if customer in djstripe db, syncs from stripe if is not
        try:
            dj_customer = sm.Customer.objects.get(id=customer.id)
        except sm.Customer.DoesNotExist:
            dj_customer = sm.Customer.sync_from_stripe_data(
                customer)

        # Checks if customer is attached to user, attach if is not
        if user.customer == dj_customer:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified\
                        customer already in database and attached to user',
                status=200
            )
        else:
            try:
                user.customer = dj_customer
                user.save()
            except Exception as e:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR : {e}',
                    status=500
                )

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Customer\
                        syncronized and attached to user',
            status=200
        )

    def handle_subscription_created(self, event):
        """ Handle customer.subscription.created webhook event from Stripe"""
        print(f'Webhook received: {event["type"]}')

        subscription = event.data.object
        school = get_object_or_404(School, pk=subscription.metadata["school"])

        # Checks if subscription in djstripe db, syncs from stripe if is not
        try:
            dj_subscription = sm.Subscription.objects.get(id=subscription.id)
        except sm.Subscription.DoesNotExist:
            dj_subscription = sm.Subscription.sync_from_stripe_data(
                subscription)

        # Checks if subscription is attached to school, attach if is not
        if school.subscription == dj_subscription:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                        Verified subscription already in database and attached\
                        to school',
                status=200
            )
        else:
            try:
                school.subscription = dj_subscription
                school.save()
            except Exception as e:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR : {e}',
                    status=500
                )

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Subscription\
                        syncronized and attached to school',
            status=200
        )

    def handle_subscription_deleted(self, event):
        """ Handle the customer.subscription.deleted webhook event
        from Stripe """

        subscription = event.data.object

        dj_subscription = get_object_or_404(
            sm.Subscription, id=subscription.id)
        dj_subscription.delete()

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Subscription\
                        deleted',
            status=200
        )
