from django.db import models
from cinema.models import Session


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.EmailField
    address = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    card_number = models.CharField(max_length=19)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField
    city = models.CharField(max_length=50)
    gender = models.BooleanField
    language = models.BooleanField


class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    seat = models.SmallIntegerField
    reservation = models.BooleanField
