from rest_framework import serializers
from .models import RandomUser


class ResponseHandling:
    def save_response(self, response_data):
        result = response_data["results"][0]
        name = result['name']
        location = result['location']
        login = result['login']
        dob = result['dob']

        RandomUser.objects.create(
            gender=result.get("gender"),
            first_name=name.get("first"),
            last_name=name.get("last"),
            street_number=location['street'].get("number"),
            street_name=location['street'].get("name"),
            city=location.get("city"),
            country=location.get("country"),
            postcode=str(location.get("postcode")),
            login=login.get("username"),
            password=login.get("password"),
            email=result.get("email"),
            born_date=dob.get("date"),
            age=dob.get("age"),
        )


class RandomUserSerializer(serializers.ModelSerializer, ResponseHandling):
    class Meta:
        model = RandomUser
        fields = (
            'gender',
            'first_name',
            'last_name',
            'street_number',
            'street_name',
            'city',
            'country',
            'postcode',
            'login',
            'password',
            'email',
            'born_date',
            'age',
        )
