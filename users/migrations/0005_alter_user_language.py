# Generated by Django 4.0.6 on 2022-08-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_gender_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('Ukrainian', 'Українська'), ('Russian', 'Русский')], max_length=10),
        ),
    ]
