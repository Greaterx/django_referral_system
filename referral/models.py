from django.db import models
from django.contrib.auth.models import User


class Referral(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_referral = models.CharField(max_length=6)
    another_referral = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=11)