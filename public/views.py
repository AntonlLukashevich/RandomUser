from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
import requests

from .models import RandomUser


class RandomUserViewSet(APIView):
    api_url = "https://randomuser.me/api/"
    permission_classes = [AllowAny]

    def post(self, request):
        info = requests.get(self.api_url).json()
        gender = info["results"][0].get("gender")
        first = info["results"][0]['name'].get("first")
        last = info["results"][0]['name'].get("last")
        street_number = info["results"][0]['location']['street'].get("number")
        street_name = info["results"][0]['location']['street'].get("name")
        city = info["results"][0]['location'].get("city")
        country = info["results"][0]['location'].get("country")
        postcode = info["results"][0]['location'].get("postcode")
        username = info["results"][0]['login'].get("username")
        password = info["results"][0]['login'].get("password")
        date = info["results"][0]['registered'].get("date")
        age = info["results"][0]['registered'].get("age")

        RandomUser.objects.create(
            gender=gender,
            first_name=first,
            last_name=last,
            street_number=street_number,
            street_name=street_name,
            city=city,
            country=country,
            postcode=str(postcode),
            login=username,
            password=password,
            born_date=date,
            age=age,
        )

        return Response(info)

    # def post(self, request):
    #     info = requests.get(self.api_url, data=json)
    #     gender = info.get('gender')
    #
    #     print(gender)
    #
    #     return Response(info)


