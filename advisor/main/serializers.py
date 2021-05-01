from rest_framework import serializers,exceptions
from .models import *
from django.contrib.auth import models,authenticate


class RegisterNewUserSerializer(serializers.Serializer):
    fname = serializers.CharField()
    # username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()


    def validate(self,data):
        fname =  data.get("fname","")
        # username =  data.get("username","")
        email = data.get("email","")
        password1 =  data.get("password1","")
        password2 =  data.get("password2","")

        if password1 == password2:
            if NewUserModel.objects.filter(email=email).exists():
                msg = "email exists"
                raise exceptions.ValidationError(msg)
            else:
                user = NewUserModel.objects.create_user(email=email, password=password1, first_name=fname)
                # user.save()
                data["user"]=user
        else:
            msg = "Passwords didnt match"
            raise exceptions.ValidationError(msg)
        return data

class AdvisorSerializor(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'