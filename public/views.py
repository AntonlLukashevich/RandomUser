import requests
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RandomUserSerializer


class RandomUserViewSet(APIView):
    permission_classes = [AllowAny]
    api_url = 'https://randomuser.me/api/'
    serializer_class = RandomUserSerializer

    def post(self, request):
        response = requests.get(self.api_url)
        info = response.json()

        user_data = info['results'][0]

        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "success"})
