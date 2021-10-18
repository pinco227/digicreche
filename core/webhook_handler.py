import djstripe.models as sm
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse


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
        customer = event.data.object
        user = get_user_model().get(email=customer.email)

        # Checks if customer in djstripe db, syncs from stripe if is not
        try:
            dj_customer = sm.Customer.get(customer.id)
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

    def handle_subscription_deleted(self, event):
        """ Handle the customer.subscription.deleted webhook event
        from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
