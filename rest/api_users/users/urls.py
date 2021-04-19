from django.urls import path
from .views import GetUser

urlpatterns = [
    path("users/", GetUser.as_view()),
]
