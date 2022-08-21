from django.contrib import admin
from .models import Banner, Banner_collection, Background_banner, Banner_news, Banner_news_collection

# Register your models here.
admin.site.register(Banner)
admin.site.register(Banner_collection)
admin.site.register(Background_banner)
admin.site.register(Banner_news)
admin.site.register(Banner_news_collection)


