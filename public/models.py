from django.db import models


class RandomUser(models.Model):
    gender = models.CharField(blank=True, verbose_name="Пол", max_length=100)
    first_name = models.CharField(blank=True, verbose_name="Имя", max_length=100)
    last_name = models.CharField(blank=True, verbose_name="Фамилия", max_length=100)
    street_number = models.IntegerField(blank=True, verbose_name="Номер улицы", null=True)
    street_name = models.CharField(blank=True, verbose_name="Улица", max_length=100)
    city = models.CharField(blank=True, verbose_name="Город проживания", max_length=100)
    country = models.CharField(blank=True, verbose_name="Страна проживания", max_length=100)
    postcode = models.CharField(blank=True, verbose_name="Почтовый индекс", max_length=100)
    login = models.CharField(blank=True, verbose_name="Логин", max_length=100)
    password = models.CharField(blank=True, verbose_name="Пароль", max_length=100)
    email = models.EmailField(blank=True, verbose_name="Почта")
    born_data = models.DateTimeField(null=True, verbose_name="Дата рождения", blank=True)
    age = models.IntegerField(blank=True, verbose_name="Возраст")
