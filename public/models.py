from django.db import models


class RandomUser(models.Model):
    gender = models.CharField(max_length=100, verbose_name="Пол", blank=True)
    first_name = models.CharField(max_length=100, verbose_name="Имя", blank=True)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", blank=True)
    street_number = models.IntegerField(verbose_name="Номер улицы", blank=True)
    street_name = models.CharField(max_length=100, verbose_name="Улица", blank=True)
    city = models.CharField(max_length=100, verbose_name="Город проживания", blank=True)
    country = models.CharField(max_length=100, verbose_name="Страна проживания", blank=True)
    postcode = models.IntegerField(verbose_name="Почтовый индекс", blank=True)
    login = models.CharField(max_length=100, verbose_name="Логин", blank=True)
    password = models.CharField(max_length=100, verbose_name="Пароль", blank=True)
    born_date = models.DateTimeField(verbose_name="Дата рождения", blank=True)
    age = models.CharField(max_length=100, verbose_name="Возраст", blank=True)

