from django.db import models
from gallery_seo.models import SEO, Image_gallery

News_promo_CHOISES = [('News', 'News'), ('Promo', 'Promo')]
# Create your models here.
class Main_page(models.Model):
    phone1 = models.CharField(max_length=19)
    phone2 = models.CharField(max_length=19)
    seo_text = models.TextField()
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class Other_page(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    main_image = models.ImageField(upload_to='pages/other')
    gallery = models.ForeignKey(Image_gallery, on_delete=models.PROTECT)
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class News_promo(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    main_image = models.ImageField(upload_to='pages/news_promo')
    gallery = models.ForeignKey(Image_gallery, on_delete=models.PROTECT)
    trailer_url = models.URLField()
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    type = models.CharField(max_length=10, choices=News_promo_CHOISES)


class Contact_page(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    coords = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='pages/contact')
