from django.core.management.base import BaseCommand
from cinema.models import Film, Hall, Session
import random
from faker import Faker
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        i = 0
        count_film = Film.objects.all()
        count_hall = Hall.objects.all()
        while i < options['numb']:
            session = Session.objects.create(
                film=random.choice(count_film),
                hall=random.choice(count_hall),
                price=random.randrange(50, 200, 5),
                date_time=fake.date_time_between_dates(datetime_start='now',
                                                       datetime_end='+10days', tzinfo=timezone.timezone.utc),
                type_3D=random.randrange(0, 1),
                type_VIP=random.randrange(0, 1),
                type_DBOX=random.randrange(0, 1),
            )
            session.save()
            i += 1
