from django.urls import path
from .views import RandomUserViewSet

urlpatterns = [
    path('randomuser/', RandomUserViewSet.as_view(), name='randomuser'),
]