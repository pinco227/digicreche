from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from django_countries import countries
from djstripe.models import Price
from core.api.serializers import PriceSerializer


class ListCountries(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all countries.
        """
        return Response(
            dict(zip(('code', 'name'), country)) for country in countries)


class PriceListAPIView(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
