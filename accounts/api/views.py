from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.api.serializers import DigiCrecheUserDisplaySerializer


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = DigiCrecheUserDisplaySerializer(request.user)
        return Response(serializer.data)
