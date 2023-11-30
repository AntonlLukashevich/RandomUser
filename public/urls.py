from django.urls import path
from .views import RandomUserViewSet

urlpatterns = [
    path('random_user/', RandomUserViewSet.as_view(), name="random_user/"),
]
