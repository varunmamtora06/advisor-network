from django.shortcuts import render
from django.contrib.auth.models import auth

#REST Auth
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

def index(request):
    pass


class RegisterNewUserView(APIView):
    def post(self, request):
        serializer = RegisterNewUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        user.save()
        return Response({
            'mssg': " registered",
        }, status=200)
