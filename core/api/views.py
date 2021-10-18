import djstripe.models as djsm
import stripe
from core.api.serializers import PriceSerializer
from django.conf import settings
from django_countries import countries
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from schools.models import School


class ListCountries(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all countries.
        """
        return Response(
            dict(zip(('code', 'name'), country)) for country in countries)


class PriceListAPIView(generics.ListAPIView):
    queryset = djsm.Price.objects.all()
    serializer_class = PriceSerializer


# https://www.saaspegasus.com/guides/django-stripe-integrate/
class CreateCustomerSubscription(APIView):
    def post(self, request):
        try:
            # parse request, extract details, and verify assumptions
            user = request.user
            school = School.objects.get(
                pk=request.data.get('schoolId'))
            email = request.data.get('email')
            assert user.email == email
            assert school.manager == user
            payment_method = request.data.get('paymentMethodId')
            priceId = request.data.get('priceId')
            stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

            # first sync payment method to local DB to workaround
            # https://github.com/dj-stripe/dj-stripe/issues/1125
            payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
            djsm.PaymentMethod.sync_from_stripe_data(payment_method_obj)

            # create customer objects
            # This creates a new Customer in stripe and attaches the default
            # PaymentMethod in one API call.
            if user.customer is None:
                customer = stripe.Customer.create(
                    payment_method=payment_method,
                    email=email,
                    invoice_settings={
                        'default_payment_method': payment_method,
                    },
                )
            else:
                customer = stripe.Customer.retrieve(user.customer.id)

            djstripe_customer = djsm.Customer.sync_from_stripe_data(
                customer)

            # create subscription
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {
                        'price': priceId,
                    },
                ],
                expand=['latest_invoice.payment_intent'],
            )
            djstripe_subscription = djsm.Subscription.sync_from_stripe_data(
                subscription)

            # associate customer and subscription with the user
            user.customer = djstripe_customer
            school.subscription = djstripe_subscription
            user.save()
            school.save()

            # return information back to the front end
            data = {
                'customer': customer,
                'subscription': subscription
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveSubscription(APIView):
    def get(self, request, *args, **kwargs):
        sub_id = kwargs.get('id')
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        subscription = stripe.Subscription.retrieve(sub_id)

        return Response(subscription, status=status.HTTP_200_OK)
