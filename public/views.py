from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from .models import RandomUser


class RandomUserViewSet(APIView):
    api_url = "https://randomuser.me/api/"
    permission_classes = [AllowAny]

    def post(self, request):
        response = requests.get(self.api_url).json()

        result = response["results"][0]
        name = result['name']
        location = result['location']
        login = result['login']
        registered = result['registered']

        data = {
            "gender": result.get("gender"),
            "first_name": name.get("first"),
            "last_name": name.get("last"),
            "street_number": location['street'].get("number"),
            "street_name": location['street'].get("name"),
            "city": location.get("city"),
            "country": location.get("country"),
            "postcode": str(location.get("postcode")),
            "login": login.get("username"),
            "password": login.get("password"),
            "email": result.get("email"),
            "born_date": registered.get("date"),
            "age": registered.get("age"),
        }

        RandomUser.objects.create(**data)

        return Response(data)
