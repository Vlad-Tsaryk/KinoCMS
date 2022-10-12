from django.core.management.base import BaseCommand
from baners.models import Background_banner, Banner_collection, Banner_news, Banner_news_collection, Banner
from pages.models import Contact_collection, Contact_page, Main_page
from gallery_seo.models import SEO
from django.core.files import File
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        i = 0
        url = 'test.com'
        if Banner_collection.objects.count() == 0:
            Banner_collection.objects.create()
        if Banner_news_collection.objects.count() == 0:
            Banner_news_collection.objects.create()
        # if Banner_news.objects.count() == 0:
        #     while i > 5:
        #         b = Banner_news()
        #         b.url = url
        #         b.image = None
        #         b.banner_news_collection = Banner_news_collection.objects.get(pk=1)
        #         i += 1
        #     i = 0
        # if Banner.objects.count() == 0:
        #     Banner.objects.create()
        if Contact_collection.objects.count() == 0:
            Contact_collection.objects.create()
        # if Contact_page.objects.count() == 0:
        #     Contact_page.objects.create()
        if Main_page.objects.count() == 0:
            m = Main_page()
            m.phone1 = '+38 (063) 111-11-11'
            m.phone2 = '+38 (098) 000-00-00'
            m.seo_text_ru = '0'
            m.seo_text_uk = '0'
            m.seo = SEO.objects.create('https://test.com','0','0','0')
            m.date = datetime.now()
        if Contact_collection.objects.count() == 0:
            Contact_collection.objects.create()