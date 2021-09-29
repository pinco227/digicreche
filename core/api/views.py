from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django_countries import countries


class ListCountries(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all countries.
        """
        return Response(
            dict(zip(('code', 'name'), country)) for country in countries)
