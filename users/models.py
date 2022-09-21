from django.core.validators import FileExtensionValidator
from django.db import models
from cinema.models import Session
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    CHOISES_language = [('uk', 'Українська'), ('ru', 'Русский')]
    CHOISES_gender = [('Male', 'Male'), ('Female', 'Female')]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150)
    # password = models.CharField(max_length=255)
    card_number = models.CharField(max_length=19)
    phone = models.CharField(max_length=19)
    birth_date = models.DateField(null=True)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=CHOISES_gender)
    language = models.CharField(max_length=10, choices=CHOISES_language)


class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    seat = models.SmallIntegerField()
    reservation = models.BooleanField()


class Mail_template(models.Model):
    template = models.FileField(upload_to='Mailing', validators=[FileExtensionValidator(['html'])])
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']
