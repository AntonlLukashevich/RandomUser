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
        data = response.json()
        self.serializer_class.save_response(data, response_data=data)

        return Response({"status": "success"})
