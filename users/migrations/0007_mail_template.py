# Generated by Django 4.0.6 on 2022-08-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail_template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.FileField(upload_to='Mailing')),
            ],
        ),
    ]
