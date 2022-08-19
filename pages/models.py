from django.db import models
from gallery_seo.models import SEO, Image_gallery


# Create your models here.
class Main_page(models.Model):
    phone1 = models.CharField(max_length=11)
    phone2 = models.CharField(max_length=11)
    seo_text = models.TextField
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class Other_page(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField
    main_image = models.ImageField
    gallery = models.ForeignKey(Image_gallery, on_delete=models.PROTECT)
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class News_promo(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    description = models.TextField
    main_image = models.ImageField
    gallery = models.ForeignKey(Image_gallery, on_delete=models.PROTECT)
    url = models.URLField
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)
    active = models.BooleanField


class Contact_page(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField
    coords = models.CharField(max_length=20)
    logo = models.ImageField
