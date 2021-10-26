from core.api import views as cv
from django.urls import path

urlpatterns = [
    path('countries/', cv.ListCountries.as_view(), name='contry-list'),
    path('prices/', cv.PlanListAPIView.as_view(), name='price-list'),
    path('create-subscription/',
         cv.CreateCustomerSubscription.as_view(), name='create-subscription'),
    path('cancel-subscription/',
         cv.CancelSubscription.as_view(), name='cancel-subscription'),
    path('update-subscription/',
         cv.UpdateSubscription.as_view(), name='update-subscription'),
    path('reactivate-subscription/',
         cv.ReactivateSubscription.as_view(), name='reactivate-subscription'),
    path('retrieve-stripe-subscription/',
         cv.RetrieveStripeSubscription.as_view(),
         name='retrieve-stripe-subscription'),
    path('retrieve-subscription/<int:pk>/',
         cv.RetrieveDBSubscription.as_view(),
         name='retrieve-subscription'),
    path('retrieve-payment-method/',
         cv.RetrievePaymentMethod.as_view(), name='retrieve-payment'),

]
