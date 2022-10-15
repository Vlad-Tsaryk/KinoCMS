from django.core.management.base import BaseCommand
from users.models import User
import random
from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='how many sessions generate')

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(options['number']):
            user = User.objects.create_user(
                address=fake.street_address(),
                city=fake.city(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone='+38 (073) 242-58-82',
                card_number=fake.credit_card_number(),
                birth_date=fake.date_of_birth(minimum_age=16, maximum_age=55),
                email=fake.email(),
                language=random.choice(['ru', 'uk']),
                gender=random.choice(['Male', 'Female']),
                password='Kinocms12345',
                username=fake.simple_profile()['username'],
            )
            print('User **'+user.username+'** successfully create')
