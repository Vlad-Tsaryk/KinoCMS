from django.core.management.base import BaseCommand
from baners.models import Background_banner, Banner_collection, Banner_news, Banner_news_collection, Banner


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Banner_collection.objects.count() == 0:
            Banner_collection.objects.create()
        if Banner_news_collection.objects.count() == 0:
            Banner_news_collection.objects.create()
        if Banner_news.objects.count() == 0:
            Banner_news.objects.create()
        if Banner.objects.count() == 0:
            Banner.objects.create()

