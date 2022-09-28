import datetime

from django.db import models
from gallery_seo.models import SEO, Image_gallery

RU_MONTH_VALUES = [
    'Января',
    'Февраля',
    'Марта',
    'Апреля',
    'Мая',
    'Июня',
    'Июля',
    'Августа',
    'Сентября',
    'Октября',
    'Ноября',
    'Декабря'
]


# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    conditions = models.TextField()
    logo = models.ImageField(upload_to='cinema')
    banner_image = models.ImageField(upload_to='cinema')
    gallery = models.ForeignKey(Image_gallery, on_delete=models.PROTECT)
    email = models.EmailField()
    phone = models.CharField(max_length=19)
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']


class Film(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.DateField(null=True)
    main_image = models.ImageField(upload_to='films')
    gallery = models.ForeignKey(Image_gallery, on_delete=models.PROTECT)
    trailer_url = models.URLField(blank=True)
    type_2D = models.BooleanField()
    type_3D = models.BooleanField()
    type_IMAX = models.BooleanField()
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']

    def get_date(self):
        return str(self.date.day) + " " + RU_MONTH_VALUES[self.date.month - 1]


class Hall(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cinema = models.ForeignKey(Cinema, on_delete=models.SET_NULL, null=True)
    scheme = models.TextField()
    banner_image = models.ImageField(upload_to='halls')
    gallery = models.ForeignKey(Image_gallery, on_delete=models.PROTECT)
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)


class Session(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    price = models.SmallIntegerField()
    date_time = models.DateTimeField()
    type_3D = models.BooleanField()
    type_DBOX = models.BooleanField()
    type_VIP = models.BooleanField()

    class Meta:
        ordering = ['date_time']
