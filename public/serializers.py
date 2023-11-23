from rest_framework import serializers
from .models import RandomUser


class RandomUserSerializer(serializers.ModelSerializer):
    def save_response(self, response_data):
        result = response_data["results"][0]
        name = result['name']
        location = result['location']
        login = result['login']
        dob = result['dob']

        data = {
            'gender': result["gender"],
            'first_name': name["first"],
            'last_name': name["last"],
            'street_number': location['street']["number"],
            'street_name': location['street']["name"],
            'city': location["city"],
            'country': location["country"],
            'postcode': location["postcode"],
            'login': login["username"],
            'password': login["password"],
            'email': result["email"],
            'born_date': dob["date"],
            'age': dob["age"],
        }

        RandomUser.objects.create(**data)

    class Meta:
        model = RandomUser
        fields = '__all__'
