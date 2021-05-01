from django.shortcuts import render
from django.contrib.auth.models import auth
from django.http import HttpResponse
#REST Auth
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .serializers import *

def index(request):
    return HttpResponse("<h1>This is a dummy index as this is just an api project</h1>")


class RegisterNewUserView(APIView):
    def post(self, request):
        serializer = RegisterNewUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        user.save()
        return Response({
            'mssg': " registered",
        }, status=200)


class AdvisorApi(APIView):

    def get(self, request, pk=None):
        if pk == None:
            advisors = Advisor.objects.all()
            serializer = AdvisorSerializor(advisors, many=True)
            return Response(serializer.data)
        else:
            advisor = Advisor.objects.get(id=pk)
            serializer = AdvisorSerializor(advisor)
            return Response(serializer.data)

    def post(self, request):
        serializer = AdvisorSerializor(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'mssg':'Data entered success'
        },status=200)

import json
class BookingApi(APIView):

    def get(self, request, user_id=None):
        bookings = Booking.objects.filter(by_user=NewUserModel.objects.get(id=user_id))
        serializer = BookingSerializor(bookings, many=True)

        # resp = {}
        advisors=[]
        # dic = {}
        for booking in bookings:
            # advisors.append(booking.advisor_booked)
            
            # dic.update({"Advisor Name":booking.advisor_booked.advisor_name,"Advisor pic":booking.advisor_booked.advisor_pic.url,"Advisor id":booking.advisor_booked.id})
            # dic.update({"Advisor pic":booking.advisor_booked.advisor_pic.url})
            # dic.update({"Advisor id":booking.advisor_booked.id})
            # print(dic)
            # advisors.append(dic)
            advisors.append({"Advisor Name":booking.advisor_booked.advisor_name,"Advisor pic":booking.advisor_booked.advisor_pic.url,"Advisor id":booking.advisor_booked.id})
            print(advisors)
        print(serializer.data)
        return Response({"booking_details":serializer.data,"advisor_details":advisors}, status=200)

    def post(self, request, user_id=None, advisor_id=None):
        serializer = BookingSerializor(data=request.data)
        serializer.is_valid(raise_exception=True)
        Booking.objects.create(booking_time=serializer.validated_data['booking_time'],advisor_booked=Advisor.objects.get(id=advisor_id), by_user=NewUserModel.objects.get(id=user_id))
        return Response(status=200)
