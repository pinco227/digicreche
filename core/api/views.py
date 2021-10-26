import djstripe.models as sm
import stripe
from core.api.permissions import IsManager
from core.api.serializers import (PaymentMethodSerializer, PlanSerializer,
                                  SubscriptionSerializer)
from django.conf import settings
from django_countries import countries
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from schools.models import School


class ListCountries(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all countries.
        """
        return Response(
            dict(zip(('code', 'name'), country)) for country in countries)


class PlanListAPIView(generics.ListAPIView):
    queryset = sm.Plan.objects.filter(active=True)
    serializer_class = PlanSerializer
    permission_classes = [IsManager]


# https://www.saaspegasus.com/guides/django-stripe-integrate/
class CreateCustomerSubscription(APIView):
    permission_classes = [IsManager]

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
            sm.PaymentMethod.sync_from_stripe_data(payment_method_obj)

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
                stripe.PaymentMethod.attach(
                    payment_method,
                    customer=user.customer.id,
                )
                customer = stripe.Customer.retrieve(user.customer.id)

            djstripe_customer = sm.Customer.sync_from_stripe_data(
                customer)

            if school.subscription is None:
                # create subscription
                subscription = stripe.Subscription.create(
                    customer=customer.id,
                    items=[
                        {
                            'price': priceId,
                        },
                    ],
                    expand=['latest_invoice.payment_intent'],
                    metadata={
                        'school': school.id,
                    },
                    trial_period_days=14,
                )
                djstripe_subscription = sm.Subscription.sync_from_stripe_data(
                    subscription)

                # associate subscription awith the school
                school.subscription = djstripe_subscription
                school.save()
            else:
                subscription = stripe.Subscription.modify(
                    school.subscription.id,
                    billing_cycle_anchor='now',
                    proration_behavior='create_prorations',
                    expand=['latest_invoice.payment_intent'],
                    default_payment_method=payment_method,
                )
                sm.Subscription.sync_from_stripe_data(subscription)

            # associate customer awith the user
            user.customer = djstripe_customer
            user.save()

            # return information back to the front end
            data = {
                'customer': customer,
                'subscription': subscription
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class UpdateSubscription(APIView):
    permission_classes = [IsManager]

    def post(self, request):
        try:
            stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

            slug = request.data.get('slug')
            school = generics.get_object_or_404(School, slug=slug)
            sub_id = school.subscription.id
            price_id = request.data.get('price_id')

            subscription = stripe.Subscription.retrieve(sub_id)

            subscription = stripe.Subscription.modify(
                sub_id,
                cancel_at_period_end=False,
                proration_behavior='create_prorations',
                items=[{
                    'id': subscription['items']['data'][0].id,
                    'price': price_id,
                }]
            )
            djstripe_subscription = sm.Subscription.sync_from_stripe_data(
                subscription)

            # associate subscription awith the school
            school.subscription = djstripe_subscription
            school.save()

            serializer = SubscriptionSerializer(djstripe_subscription)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)


class CancelSubscription(APIView):
    permission_classes = [IsManager]

    def post(self, request):
        try:
            stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
            slug = request.data.get('slug')
            school = generics.get_object_or_404(School, slug=slug)
            sub_id = school.subscription.id
            subscription = stripe.Subscription.modify(
                sub_id,
                cancel_at_period_end=True
            )
            djstripe_subscription = sm.Subscription.sync_from_stripe_data(
                subscription)

            # associate subscription awith the school
            school.subscription = djstripe_subscription
            school.save()

            serializer = SubscriptionSerializer(djstripe_subscription)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)


class ReactivateSubscription(APIView):
    permission_classes = [IsManager]

    def post(self, request):
        try:
            stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
            slug = request.data.get('slug')
            school = generics.get_object_or_404(School, slug=slug)
            sub_id = school.subscription.id
            subscription = stripe.Subscription.modify(
                sub_id,
                cancel_at_period_end=True
            )
            subscription = stripe.Subscription.modify(
                sub_id,
                cancel_at_period_end=False,
            )
            djstripe_subscription = sm.Subscription.sync_from_stripe_data(
                subscription)

            # associate subscription awith the school
            school.subscription = djstripe_subscription
            school.save()

            serializer = SubscriptionSerializer(djstripe_subscription)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveStripeSubscription(APIView):
    permission_classes = [IsManager]

    def post(self, request):
        sub_id = request.data.get('id')
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        subscription = stripe.Subscription.retrieve(sub_id)

        return Response(subscription, status=status.HTTP_200_OK)


class RetrieveDBSubscription(generics.RetrieveAPIView):
    queryset = sm.Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsManager]


class RetrievePaymentMethod(APIView):
    permission_classes = [IsManager]

    def post(self, request):
        try:
            user = request.user
            pm_id = (
                user.customer.invoice_settings['default_payment_method'])
            paymentMethod = generics.get_object_or_404(sm.PaymentMethod,
                                                       id=pm_id)
            serializer = PaymentMethodSerializer(paymentMethod)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)
