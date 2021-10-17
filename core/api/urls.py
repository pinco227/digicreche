from django.urls import path
from core.api import views as cv

urlpatterns = [
    path('countries/', cv.ListCountries.as_view(), name='contry-list'),
    path('prices/', cv.PriceListAPIView.as_view(), name='price-list'),
    path('create-subscription/',
         cv.CreateCustomerSubscription.as_view(), name='create-subscription'),
    path('retrieve-subscription/<id>/',
         cv.RetrieveSubscription.as_view(), name='retrieve-subscription'),

]
