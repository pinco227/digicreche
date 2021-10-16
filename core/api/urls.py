from django.urls import path
from core.api import views as cv

urlpatterns = [
    path('countries/', cv.ListCountries.as_view(), name='contry-list'),
    path('prices/', cv.PriceListAPIView.as_view(), name='price-list'),
]
