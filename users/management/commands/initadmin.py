from django.core.management.base import BaseCommand
from users.models import User
from faker import Faker
from random import choice


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        if User.objects.count() == 0:
            username = 'admin'
            email = 'adminemail@gmail.com'
            password = '0'
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(
                email=email,
                username=username,
                password=password,
                address=fake.street_address(),
                city=fake.city(),
                first_name='admin',
                last_name='admin',
                phone='+38 (073) 111-11-11',
                card_number=fake.credit_card_number(),
                birth_date=fake.date_of_birth(minimum_age=16, maximum_age=55),
                language=choice(['ru', 'uk']),
                gender=choice(['Male', 'Female'])
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
