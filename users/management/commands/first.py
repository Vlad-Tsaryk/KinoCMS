from django.core.management.base import BaseCommand
from baners.models import Background_banner, Banner_collection, Banner_news, Banner_news_collection, Banner
from pages.models import Contact_collection, Contact_page, Main_page, Other_page
from cinema.models import Film, Cinema, Hall, Session
from users.models import Mail_template
from gallery_seo.models import SEO, Image_gallery
from datetime import datetime
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        url = 'test.com'
        if Banner_collection.objects.count() == 0:
            Banner_collection.objects.create()
            print('Banner_collection create successful')
        if Banner_news_collection.objects.count() == 0:
            Banner_news_collection.objects.create()
            print('Banner_news_collection create successful')
        if Background_banner.objects.count() == 0:
            Background_banner.objects.create(color=fake.hex_color(), image='static_kit/bg_banner/1.png',
                                             is_image=True)
            print('Background_banner create successful')
        if Banner_news.objects.count() == 0:
            for index in range(2):
                b = Banner_news()
                b.url = url
                b.image = f'static_kit/banners/news_promo/{index + 1}.png'
                b.banner_news_collection = Banner_news_collection.objects.get(pk=1)
                b.save()
            print('Banner_news create successful')
        if Banner.objects.count() == 0:
            for index in range(4):
                b = Banner()
                b.url = url
                b.text = 'Test'
                b.image = f'static_kit/banners/{index + 1}.jpg'
                b.banner_news_collection = Banner_news_collection.objects.get(pk=1)
                b.save()
            print('Banners create successful')
        if Contact_collection.objects.count() == 0:
            Contact_collection.objects.create(seo=SEO.objects.create(url=url, description='0', keywords='0', title='0'))
            print('Contact_collection create successful')
        if Contact_page.objects.count() == 0:
            for index in range(3):
                contact = Contact_page()
                contact.name_ru = 'Multiplex'
                contact.name_uk = 'Multiplex'
                contact.address_ru = 'Multiplex'
                contact.address_uk = 'Multiplex'
                contact.logo = f'static_kit/pages/contact/{index + 1}.jpg'
                contact.coords = '<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2482.' \
                                 '882221238436!2d31.30413268731127!3d51.515376752843494!3m2!1i1024!2i768!' \
                                 '4f13.1!3m3!1m2!1s0x0%3A0x279389079807cbdc!2sMultiplex%20Cinema%20(Hollywood)!' \
                                 '5e0!3m2!1sru!2sua!4v1662543668527!5m2!1sru!2sua" width="600" height="450"' \
                                 ' style="border:0;" allowfullscreen="" loading="lazy" ' \
                                 'referrerpolicy="no-referrer-when-downgrade"></iframe>'
                contact.contact_collection = Contact_collection.objects.first()
                contact.save()

        if Main_page.objects.count() == 0:
            m = Main_page()
            m.phone1 = '+38 (063) 111-11-11'
            m.phone2 = '+38 (098) 000-00-00'
            m.seo_text_ru = fake.text(max_nb_chars=500)
            m.seo_text_uk = fake.text(max_nb_chars=500)
            m.seo = SEO.objects.create(url=url, description='0', keywords='0', title='0')
            m.date = datetime.today()
            m.save()
            print('Main_page create successful')
        if Contact_collection.objects.count() == 0:
            Contact_collection.objects.create()
            print('Contact_collection create successful')
        if Other_page.objects.count() == 0:
            pages = [['Vip-зал', 'Vip-зал'], ['Детская комната', 'Дитяча кімната'], ['Кафе-бар', 'Кафе-бар'],
                     ['О кинотеатре', 'Про кінотеатр'], ['Реклама', 'Реклама']]
            for name in pages:
                page = Other_page()
                page.seo = SEO.objects.create(url=url, description='0', keywords='0', title='0')
                page.name_ru = name[0]
                page.name_uk = name[1]
                page.description_ru = fake.text(max_nb_chars=500)
                page.description_uk = fake.text(max_nb_chars=500)
                page.main_image = 'static_kit/pages/unnamed.png'
                page.gallery = Image_gallery.objects.create()
                page.save()
            print('Pages create successful')
        if Cinema.objects.count() == 0:
            cinema_names = [['Multiplex Hollywood', 'Multiplex Hollywood'],
                            ['Multiplex RiverMall', 'Multiplex RiverMall'],
                            ['Планета Кино', 'Планета Кіно']]
            for index, name in cinema_names:
                cinema = Cinema()
                cinema.seo = SEO.objects.create(url=url, description='0', keywords='0', title='0')
                cinema.name_ru = name[0]
                cinema.name_uk = name[1]
                cinema.description_ru = fake.text(max_nb_chars=500)
                cinema.description_uk = fake.text(max_nb_chars=500)
                cinema.email = fake.email()
                cinema.conditions_ru = fake.text(max_nb_chars=500)
                cinema.conditions_uk = fake.text(max_nb_chars=500)
                cinema.phone = '+38 (098) 000-00-00'
                cinema.logo = f'static_kit/cinema/logo/{index + 1}.png'
                cinema.banner_image = f'static_kit/cinema/{index + 1}.jpg'
                cinema.gallery = Image_gallery.objects.create()
                cinema.save()
            print('Cinemas create successful')
        if Hall.objects.count() == 0:
            cinemas = Cinema.objects.all()
            for cinema in cinemas:
                for index in range(2):
                    hall = Hall()
                    hall.cinema = cinema
                    hall.scheme = '{1: 5,2: 10,3: 12,4: 15,5: 5,6: 18,7: 6,}'
                    hall.seo = SEO.objects.create(url=url, description='0', keywords='0', title='0')
                    hall.gallery = Image_gallery.objects.create()
                    hall.name_ru = str(index + 1)
                    hall.name_uk = str(index + 1)
                    hall.description_ru = fake.text(max_nb_chars=500)
                    hall.description_uk = fake.text(max_nb_chars=500)
                    hall.banner_image = f'static_kit/hall/{index + 1}.jpg'
                    hall.save()
            print('Halls create successful')
        if Film.objects.count() == 0:
            films_names = [['Варяг', 'Варяг'], ['Добыча', 'Здобич'],
                           ['Доктор Стрендж', 'Доктор Стрендж'],
                           ['Лу', 'Лу'], ['Мир Юрского периода: Господство', 'Світ Юрського періоду 3: Домініон'],
                           ['Самаритянин', 'Самаритянин'], ['Снайпер', 'Снайпер'],
                           ['Топ Ган: Мэверик', 'Топ Ґан: Меверік'], ['Человек из торонто', 'Людина з торонто'],
                           ['Черний телефон', 'Чорний телефон']]
            films_trailer_url = ["https://www.youtube.com/embed/oMSdFM12hOw",
                                 "https://www.youtube.com/embed/wZ7LytagKlc",
                                 "https://www.youtube.com/embed/aWzlQ2N6qqg",
                                 "https://www.youtube.com/embed/QILhvR4QPsQ",
                                 "https://www.youtube.com/embed/fb5ELWi-ekk",
                                 "https://www.youtube.com/embed/9FKnTxSC16E",
                                 "https://www.youtube.com/embed/VptIeP_TpTU",
                                 "https://www.youtube.com/embed/g4U4BQW9OEk",
                                 "https://www.youtube.com/embed/urqy8DrcGBs",
                                 "https://www.youtube.com/embed/wvhDQO1uuTQ"]
            for index, name in films_names:
                film = Film()
                film.name_ru = name[0]
                film.name_uk = name[1]
                film.description_ru = fake.text(max_nb_chars=500)
                film.description_uk = fake.text(max_nb_chars=500)
                film.date = fake.date_between_dates(datetime_start='-10days', datetime_end='+10days')
                film.main_image = f'static_kit/films/{index + 1}.png'
                film.gallery = Image_gallery.objects.create()
                film.trailer_url = films_trailer_url[index]
                film.type_IMAX = fake.pybool()
                film.type_3D = fake.pybool()
                film.type_2D = fake.pybool()
                film.save()
        if Mail_template.objects.count() == 0:
            Mail_template.objects.create(template=f'static_kit/emails/test.html')
            Mail_template.objects.create(template=f'static_kit/emails/mail.html')