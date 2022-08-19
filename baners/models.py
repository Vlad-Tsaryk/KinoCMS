from django.db import models


# Create your models here.
class Background_banner(models.Model):
    image = models.ImageField(upload_to='banner')
    color = models.CharField(max_length=7)
    is_image = models.BooleanField(default=True)


class Banner_collection(models.Model):
    rotation_speed = models.TimeField()
    active = models.CharField(max_length=10)


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/', null=True, blank=True)
    url = models.URLField()
    text = models.CharField(max_length=100)
    banner_collection = models.ForeignKey(Banner_collection, on_delete=models.PROTECT)


class Banner_news_collection(models.Model):
    rotation_speed = models.TimeField()
    active = models.BooleanField()


class Banner_news(models.Model):
    image = models.ImageField(upload_to='banner')
    url = models.URLField()
    banner_news_collection = models.ForeignKey(Banner_news_collection, on_delete=models.PROTECT)
