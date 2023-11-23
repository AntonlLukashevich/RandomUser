from django.urls import path
from .views import RandomUserViewSet

urlpatterns = [
    path('random-user/', RandomUserViewSet.as_view(), name='random-user'),
]
