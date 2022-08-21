import datetime

from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Film, Hall, Cinema
from .forms import FilmForm, CinemaForm, HallFormSet, HallForm
from gallery_seo.forms import SeoForm, GalleryForm, ImageFormSet
from gallery_seo.forms import Image


# Create your views here.

def index(request):
    return render(request, 'layout/basic.html')


def films(request):
    date = datetime.date.today()
    films_now = Film.objects.filter(date__lte=date)
    films_soon = Film.objects.filter(date__gt=date).order_by('date')[:5]
    context = {"films": films_now, 'films_soon': films_soon}
    return render(request, 'cinema/films.html', context)


def add_film(request):
    if request.method == 'POST':
        seo_form = SeoForm(request.POST)
        film_form = FilmForm(request.POST, request.FILES)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        print(request.POST, request.FILES)
        if all([film_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            film = film_form.save(commit=False)
            images = image_form_set.save(commit=False)
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            film.seo = seo

            for image in images:
                if image.image:
                    image.galleryId = gallery
                    image.save()

            film.gallery = gallery
            film.save()
            print(request.POST, request.FILES)
            return redirect('films')
    else:
        print('no valid')
        image_form_set = ImageFormSet(queryset=Image.objects.none())
        film_form = FilmForm()
        seo_form = SeoForm()
    return render(request, 'cinema/film_create.html', {'film_form': film_form, 'seo_form': seo_form,
                                                       'images_formset': image_form_set,
                                                       })


def film_update(request, film_id):
    obj = get_object_or_404(Film, id=film_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    if request.method == 'POST':
        film_form = FilmForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo)
        print(request.POST, request.FILES)
        if all([film_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            film = film_form.save(commit=False)
            images = image_form_set.save(commit=False)
            film.seo = seo
            print(image_form_set.deleted_objects)
            for del_image in image_form_set.deleted_objects:
                print(del_image)
                del_image.delete()

            for image in images:
                if image.image:
                    image.galleryId = film.gallery
                    image.save()
            film.save()
            print(request.POST, request.FILES)
            return redirect('films')
    else:
        print('no valid')
        image_form_set = ImageFormSet(queryset=gallery_qs)
        film_form = FilmForm(instance=obj)
        seo_form = SeoForm(instance=obj.seo)
    return render(request, 'cinema/film_update.html', {'film_form': film_form, 'seo_form': seo_form,
                                                       'images_formset': image_form_set,
                                                       })


def add_cinema(request):
    print(request.POST, request.FILES)
    if request.method == 'POST':
        # hall_form_set = HallFormSet(request.POST, queryset=Hall.objects.none())
        seo_form = SeoForm(request.POST)
        cimena_form = CinemaForm(request.POST, request.FILES)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if all([seo_form.is_valid(), cimena_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            cimena = cimena_form.save(commit=False)
            images = image_form_set.save(commit=False)
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            cimena.seo = seo
            for image in images:
                if image.image:
                    image.galleryId = gallery
                    image.save()

            cimena.gallery = gallery
            cimena.save()
            print(request.POST, request.FILES)
            return redirect('cinemas')

    else:
        print('not valid')
        print(request.POST, request.FILES)
        seo_form = SeoForm()
        cimena_form = CinemaForm()
        image_form_set = ImageFormSet(queryset=Image.objects.none())
        # hall_form_set = HallFormSet(queryset=Hall.objects.none())
    context = {'cinema_form': cimena_form, 'images_formset': image_form_set, 'seo_form': seo_form}

    return render(request, 'cinema/cinema_create.html', context)


def cinemas(request):
    cinemas = Cinema.objects.all()
    context = {"cinemas": cinemas}
    return render(request, 'cinema/cinemas.html', context)


def cinema_update(request, cinema_id):
    obj = get_object_or_404(Cinema, id=cinema_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    halls = Hall.objects.filter(cinema_id=cinema_id)
    if request.method == 'POST':
        cinema_form = CinemaForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo)
        print(request.POST, request.FILES)
        if all([cinema_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            cinema = cinema_form.save(commit=False)
            images = image_form_set.save(commit=False)
            cinema.seo = seo
            for del_image in image_form_set.deleted_objects:
                print(del_image)
                del_image.delete()

            for image in images:
                if image.image:
                    image.galleryId = cinema.gallery
                    image.save()
            cinema.save()
            print(request.POST, request.FILES)
            return redirect('cinemas')
    else:
        print('no valid')
        image_form_set = ImageFormSet(queryset=gallery_qs)
        cinema_form = CinemaForm(instance=obj)
        seo_form = SeoForm(instance=obj.seo)

    context = {'cinema_form': cinema_form,
               'seo_form': seo_form,
               'images_formset': image_form_set,
               'halls': halls}
    return render(request, 'cinema/cinema_update.html', context)


def add_hall(request, cinema_id):
    if request.method == 'POST':
        hall_form = HallForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        print(request.POST, request.FILES)
        if all([seo_form.is_valid(), hall_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            hall = hall_form.save(commit=False)
            images = image_form_set.save(commit=False)
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            hall.seo = seo
            hall.cinema = Cinema.objects.get(pk=cinema_id)
            for image in images:
                if image.image:
                    image.galleryId = gallery
                    image.save()

            hall.gallery = gallery
            hall.save()
            print(request.POST, request.FILES)
            return redirect('cinema_update', cinema_id)
    else:
        print('not valid')
        hall_form = HallForm()
        seo_form = SeoForm()
        image_form_set = ImageFormSet(queryset=Image.objects.none())
    context = {'hall_form': hall_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'cinema/hall_create.html', context)


def hall_update(request, cinema_id, hall_id):
    obj = get_object_or_404(Hall, id=hall_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    if request.method == 'POST':
        hall_form = HallForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo)
        print(request.POST, request.FILES)
        if all([hall_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            hall = hall_form.save(commit=False)
            images = image_form_set.save(commit=False)
            hall.seo = seo
            for del_image in image_form_set.deleted_objects:
                print(del_image)
                del_image.delete()
            for image in images:
                if image.image:
                    image.galleryId = hall.gallery
                    image.save()
            hall.save()
            print(request.POST, request.FILES)
            return redirect('cinema_update', cinema_id)
    else:
        print('no valid')
        image_form_set = ImageFormSet(queryset=gallery_qs)
        hall_form = HallForm(instance=obj)
        seo_form = SeoForm(instance=obj.seo)

    context = {'hall_form': hall_form,
               'seo_form': seo_form,
               'images_formset': image_form_set}
    return render(request, 'cinema/hall_update.html', context)


def delete_hall(request, hall_id, cinema_id):
    hall = Hall.objects.get(id=hall_id)
    hall.delete()
    return redirect('cinema_update', cinema_id)
