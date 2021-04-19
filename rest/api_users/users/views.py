from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

# Create your views here.


class GetUser(APIView):

    def get(self, request, *args, **kwargs):
        user = {"name":"Rodrigo", "last_name":"Urcino", "email":"francisco@miflink.com", "age":25, "phone":7411196882}
        return Response(status=HTTP_200_OK, data=user)