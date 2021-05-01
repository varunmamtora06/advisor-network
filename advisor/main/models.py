from django.db import models
from django.contrib.auth import models as mod
# Create your models here.

class Advisor(models.Model):
    advisor_name = models.CharField(max_length=50)
    advisor_pic = models.ImageField(upload_to='advisorPics/', blank=True)

class Booking(models.Model):
    booking_time = models.DateTimeField(auto_now_add=False)
    advisor_booked = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    by_user = models.ForeignKey(mod.User, on_delete=models.CASCADE)
