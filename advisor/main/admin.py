from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(NewUserModel)
class NewUserAdmin(admin.ModelAdmin):
    list_display=['id','first_name','email']

@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display=['id','advisor_name']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=['id','booking_time','advisor_booked', 'by_user']
