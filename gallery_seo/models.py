from django.db import models


# Create your models here.

class Image_gallery(models.Model):
    class Meta:
        verbose_name = 'Gallery'


class Image(models.Model):
    image = models.ImageField(upload_to='gallery')
    galleryId = models.ForeignKey(Image_gallery, on_delete=models.PROTECT, blank= True)


# class Image_gallery(models.Model):
#     images = models.ManyToManyField(Image)

class SEO(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    description = models.TextField()
