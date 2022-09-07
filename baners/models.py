from django.db import models

Rotation_Speed_CHOISES = [('5000', '5s'),
                          ('10000', '10s'),
                          ('15000', '15s'),
                          ('20000', '20s'),
                          ('30000', '30s'),
                          ('45000', '45s'),
                          ('60000', '1m'),
                          ('120000', '2m'),
                          ('300000', '5m'),
                          ]


# Create your models here.
class Background_banner(models.Model):
    image = models.ImageField(upload_to='banner')
    color = models.CharField(max_length=7)
    is_image = models.BooleanField(default=True)


class Banner_collection(models.Model):
    rotation_speed = models.CharField(max_length=10, choices=Rotation_Speed_CHOISES, default='5s')
    active = models.BooleanField(default=True)


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/', null=True, blank=True)
    url = models.URLField()
    text = models.CharField(max_length=100)
    banner_collection = models.ForeignKey(Banner_collection, on_delete=models.PROTECT)


class Banner_news_collection(models.Model):
    rotation_speed = models.CharField(max_length=10, choices=Rotation_Speed_CHOISES, default='5s')
    active = models.BooleanField(default=True)


class Banner_news(models.Model):
    image = models.ImageField(upload_to='banner')
    url = models.URLField()
    banner_news_collection = models.ForeignKey(Banner_news_collection, on_delete=models.PROTECT)
