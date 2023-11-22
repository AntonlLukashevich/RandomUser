from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from .serializers import RandomUserSerializer


class RandomUserViewSet(APIView):
    api_url = "https://randomuser.me/api/"
    permission_classes = [AllowAny]
    serializer_class = RandomUserSerializer

    def post(self, request):
        response = requests.get(self.api_url)
        self.serializer_class.save_response(response.json(), response_data=response.json())

        return Response({"status": "success"})
