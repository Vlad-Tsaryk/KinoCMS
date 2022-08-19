from django.db import models
from gallery_seo.models import SEO, Image_gallery


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


class Hall(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cinema = models.OneToOneField(Cinema, on_delete=models.SET_NULL, null=True)
    scheme = models.ImageField(upload_to='halls')
    banner_image = models.ImageField(upload_to='halls')
    gallery = models.ForeignKey(Image_gallery, on_delete=models.PROTECT)
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class Session(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    price = models.SmallIntegerField()
    time = models.TimeField()
    type_3D = models.BooleanField()
    type_DBOX = models.BooleanField()
    type_VIP = models.BooleanField()
