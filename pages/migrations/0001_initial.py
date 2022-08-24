# Generated by Django 4.0.6 on 2022-08-23 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery_seo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.seo')),
            ],
        ),
        migrations.CreateModel(
            name='Other_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('main_image', models.ImageField(upload_to='pages/other')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.image_gallery')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.seo')),
            ],
        ),
        migrations.CreateModel(
            name='News_promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('main_image', models.ImageField(upload_to='pages/news_promo')),
                ('trailer_url', models.URLField()),
                ('active', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('News', 'News'), ('Promo', 'Promo')], max_length=10)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.image_gallery')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.seo')),
            ],
        ),
        migrations.CreateModel(
            name='Main_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('phone1', models.CharField(max_length=19)),
                ('phone2', models.CharField(max_length=19)),
                ('seo_text', models.TextField()),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gallery_seo.seo')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('coords', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='pages/contact')),
                ('contact_collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pages.contact_collection')),
            ],
        ),
    ]
