from django.core.management.base import BaseCommand
from baners.models import Background_banner, Banner_collection, Banner_news, Banner_news_collection, Banner
from django.core.files import File


class Command(BaseCommand):
    def handle(self, *args, **options):
        i = 0
        url = 'test.com'
        if Banner_collection.objects.count() == 0:
            Banner_collection.objects.create()
        if Banner_news_collection.objects.count() == 0:
            Banner_news_collection.objects.create()
        if Banner_news.objects.count() == 0:
            while i > 5:
                b = Banner_news()
                b.url = url
                b.image = None
                b.banner_news_collection = Banner_news_collection.objects.get(pk=1)
                i += 1
            i = 0
        if Banner.objects.count() == 0:
            Banner.objects.create()
