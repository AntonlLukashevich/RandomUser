from rest_framework import serializers
from .models import RandomUser


class RandomUserSerializer(serializers.Serializer):
    gender = serializers.CharField(max_length=100, label="Пол")
    first_name = serializers.CharField(max_length=100, label="Имя", required=False)
    last_name = serializers.CharField(max_length=100, label="Фамилия", required=False)
    street_number = serializers.IntegerField(label="Номер улицы", required=False, allow_null=True)
    street_name = serializers.CharField(max_length=100, label="Улица", required=False)
    city = serializers.CharField(max_length=100, label="Город проживания", required=False)
    country = serializers.CharField(max_length=100, label="Страна проживания", required=False)
    postcode = serializers.CharField(max_length=100, label="Почтовый индекс", required=False)
    login = serializers.CharField(max_length=100, label="Логин", required=False)
    password = serializers.CharField(max_length=100, label="Пароль", required=False)
    email = serializers.EmailField(label="Почта", required=False)
    born_data = serializers.DateTimeField(label="Дата рождения", required=False)
    age = serializers.IntegerField(label="Возраст", required=False)

    def to_internal_value(self, data):
        return {
            "gender": data.get('gender'),
            "first_name": data.get('name', {}).get('first', ''),
            "last_name": data.get('name', {}).get('last', ''),
            "street_number": data.get('location', {}).get('street', {}).get('number'),
            "street_name": data.get('location', {}).get('street', {}).get('name', ''),
            "city": data.get('location', {}).get('city', ''),
            "country": data.get('location', {}).get('country', ''),
            "postcode": data.get('location', {}).get('postcode', ''),
            "login": data.get('login', {}).get('username', ''),
            "password": data.get('login', {}).get('password', ''),
            "email": data.get('email'),
            "born_data": data.get('dob', {}).get('date'),
            "age": data.get('dob', {}).get('age'),
        }

    def create(self, validated_data):
        return RandomUser.objects.create(**validated_data)
