import datetime
import json
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from KinoCMS.settings import BASE_DIR
from .models import Film, Hall, Cinema, RU_MONTH_VALUES, Session
from .forms import FilmForm, CinemaForm, HallFormSet, HallForm
from gallery_seo.forms import SeoForm, GalleryForm, ImageFormSet
from gallery_seo.forms import Image
from pages.models import Other_page
from django.contrib.auth.decorators import login_required, user_passes_test
from baners.models import Background_banner, Banner, Banner_collection, Banner_news, Banner_news_collection
from pages.models import Main_page, News_promo
from users.models import Ticket
import locale


# Create your views here.
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def films(request):
    date = datetime.date.today()
    films_now = Film.objects.filter(date__lte=date)
    films_soon = Film.objects.filter(date__gt=date).order_by('date')[:5]
    print(request)
    context = {"films": films_now, 'films_soon': films_soon}
    return render(request, 'cinema/films.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def add_film(request):
    if request.method == 'POST':
        seo_form = SeoForm(request.POST, prefix='seo')
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
        seo_form = SeoForm(prefix='seo')
    return render(request, 'cinema/film_create.html', {'film_form': film_form, 'seo_form': seo_form,
                                                       'images_formset': image_form_set,
                                                       })


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def film_update(request, film_id):
    obj = get_object_or_404(Film, id=film_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    if request.method == 'POST':
        film_form = FilmForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo, prefix='seo')
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
        seo_form = SeoForm(instance=obj.seo, prefix='seo')
    return render(request, 'cinema/film_update.html', {'film_form': film_form, 'seo_form': seo_form,
                                                       'images_formset': image_form_set,
                                                       })


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def add_cinema(request):
    print(request.POST, request.FILES)
    if request.method == 'POST':
        # hall_form_set = HallFormSet(request.POST, queryset=Hall.objects.none())
        seo_form = SeoForm(request.POST, prefix='seo')
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
        seo_form = SeoForm(prefix='seo')
        cimena_form = CinemaForm()
        image_form_set = ImageFormSet(queryset=Image.objects.none())
        # hall_form_set = HallFormSet(queryset=Hall.objects.none())
    context = {'cinema_form': cimena_form, 'images_formset': image_form_set, 'seo_form': seo_form}

    return render(request, 'cinema/cinema_create.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def cinemas(request):
    cinemas = Cinema.objects.all()
    context = {"cinemas": cinemas}
    return render(request, 'cinema/cinemas.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def cinema_update(request, cinema_id):
    obj = get_object_or_404(Cinema, id=cinema_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    halls = Hall.objects.filter(cinema_id=cinema_id).order_by('name')
    if request.method == 'POST':
        cinema_form = CinemaForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo, prefix='seo')
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
        seo_form = SeoForm(instance=obj.seo, prefix='seo')

    context = {'cinema_form': cinema_form,
               'seo_form': seo_form,
               'images_formset': image_form_set,
               'halls': halls}
    return render(request, 'cinema/cinema_update.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def delete_cinema(request, cinema_id):
    obj_cinema = Cinema.objects.get(pk=cinema_id)
    obj_cinema.delete()
    return redirect('cinemas')


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def add_hall(request, cinema_id):
    if request.method == 'POST':
        hall_form = HallForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST, prefix='seo')
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
        seo_form = SeoForm(prefix='seo')
        image_form_set = ImageFormSet(queryset=Image.objects.none())
    context = {'hall_form': hall_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'cinema/hall_create.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def hall_update(request, cinema_id, hall_id):
    obj = get_object_or_404(Hall, id=hall_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    if request.method == 'POST':
        hall_form = HallForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo, prefix='seo')
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
        seo_form = SeoForm(instance=obj.seo, prefix='seo')

    context = {'hall_form': hall_form,
               'seo_form': seo_form,
               'images_formset': image_form_set}
    return render(request, 'cinema/hall_update.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def delete_hall(request, hall_id, cinema_id):
    hall = Hall.objects.get(id=hall_id)
    hall.delete()
    return redirect('cinema_update', cinema_id)


def kino_cms(request):
    today = datetime.datetime.today()
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    films_today = Film.objects.filter(date__lte=today)
    films_soon = Film.objects.filter(date__gt=today)
    back_banner = Background_banner.objects.get(pk=1)
    banners = Banner.objects.all()
    banners_collection = Banner_collection.objects.get(pk=1)
    banners_news = Banner_news.objects.all()
    banners_news_collection = Banner_news_collection.objects.get(pk=1)
    print(datetime.date.month)
    current_day = str(today.day) + " " + RU_MONTH_VALUES[today.month - 1]
    context = {'films_today': films_today, 'films_soon': films_soon, 'back_banner': back_banner, 'banners': banners,
               'main_page': main_page, 'current_day': current_day, 'banners_news': banners_news,
               'banners_collection': banners_collection, 'banners_news_collection': banners_news_collection,
               'pages': page_list
               }
    return render(request, 'layout/KinoCMS.html', context)


def movies(request):
    films_today = Film.objects.filter(date__lte=datetime.datetime.today())
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    context = {'films_today': films_today, 'main_page': main_page, 'pages': page_list}
    return render(request, 'cinema/movies.html', context)


def soon(request):
    films_soon = Film.objects.filter(date__gt=datetime.datetime.today())
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    context = {'films_soon': films_soon, 'main_page': main_page, 'pages': page_list}
    return render(request, 'cinema/soon.html', context)


def cinemas_page(request):
    obj_cinemas = Cinema.objects.all()
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    context = {'cinemas': obj_cinemas, 'main_page': main_page, 'pages': page_list}
    return render(request, 'cinema/cinemas_site.html', context)


def showtimes(request):
    today = datetime.datetime.today()
    print(today)
    sessions = Session.objects.filter(date_time__gt=today).values('pk', 'film__name', 'hall__cinema__name',
                                                                  'hall__name', 'price',
                                                                  'date_time__time', 'date_time')

    cinemas_names = []
    films_names = []
    print(sessions)
    for s in sessions:
        s['date_time'] = s['date_time'].strftime("%d.%m.%Y")
        if s['hall__cinema__name'] not in cinemas_names:
            cinemas_names.append(s['hall__cinema__name'])
        if s['film__name'] not in films_names:
            films_names.append(s['film__name'])
    sessions_list = list(sessions)
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'GET':
            return JsonResponse({'sessions': sessions_list})

    context = {'main_page': main_page, 'cinemas_names': cinemas_names, 'films_names': films_names, 'pages': page_list}
    return render(request, 'cinema/showtimes.html', context)


def film_card(request, film_id):
    today = datetime.datetime.today()
    obj_films = Film.objects.get(pk=film_id)
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    film_sessions = Session.objects.filter(film_id=film_id)
    film_gallery = Image.objects.filter(galleryId=obj_films.gallery.pk)
    cinemas_dict = {}
    session_dates = []
    for cinema in film_sessions.order_by('hall__cinema__name').values('hall__cinema__name',
                                                                      'hall__cinema_id').distinct():
        cinemas_dict[cinema['hall__cinema__name']] = cinema['hall__cinema_id']
    for s in film_sessions:
        if s.date_time.astimezone().date() not in session_dates:
            session_dates.append(s.date_time.astimezone().date())
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = json.load(request)
        cinema = data.get('cinema')
        if request.method == 'POST':
            try:
                date = datetime.datetime.strptime(data.get('date'), '%Y-%m-%d')
                date = date.astimezone().date()
                filter_sessions_by_date = film_sessions.filter(hall__cinema_id=cinema, date_time__day=date.day,
                                                               date_time__month=date.month,
                                                               date_time__year=date.year).order_by('date_time')
                return JsonResponse({'filter_sessions': list(filter_sessions_by_date.values('id', 'hall__name',
                                                                                            'date_time',
                                                                                            'price'))})
            except:
                filter_sessions_by_cinema = film_sessions.filter(hall__cinema_id=cinema)
                filter_dates = []
                for session in filter_sessions_by_cinema:
                    if session.date_time.astimezone().date() not in filter_dates:
                        filter_dates.append(session.date_time.astimezone().date())
                return JsonResponse({'filter_dates': filter_dates})
    context = {'film': obj_films, 'main_page': main_page, 'cinemas_dict': cinemas_dict, 'session_dates': session_dates,
               'film_gallery': film_gallery, 'pages': page_list}
    return render(request, 'cinema/film_card.html', context)


@login_required()
def seat_reservation(request, session_id):
    page_list = Other_page.objects.all()
    main_page = Main_page.objects.get(pk=1)
    obj_session = Session.objects.get(pk=session_id)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        sold_out = []
        if request.method == 'POST':
            data = json.load(request)
            seats = data.get('seats')
            reservation = data.get('reserved')
            for seat in seats:
                ticket = Ticket(session_id=session_id, user_id=request.user.pk, seat=seat, reservation=reservation)
                ticket.save()
            tickets = Ticket.objects.filter(session=obj_session).values('seat')
            for ticket in tickets:
                sold_out.append(ticket['seat'])
            return JsonResponse({'sold_out': sold_out})
        if request.method == 'GET':
            tickets = Ticket.objects.filter(session=obj_session).values('seat')
            for ticket in tickets:
                sold_out.append(ticket['seat'])
            return JsonResponse({'sold_out': sold_out})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    context = {'session': obj_session, 'pages': page_list, 'main_page': main_page}
    return render(request, 'cinema/seat_reservation.html', context)


def cinema_card(request, cinema_id):
    date = datetime.date.today()
    sessions = Session.objects.filter(date_time__day=date.day,
                                      date_time__month=date.month,
                                      date_time__year=date.year)
    sessions_today = []
    for session in sessions:
        if session.film.name not in sessions_today:
            sessions_today.append(session.film.name)
    page_list = Other_page.objects.all()
    main_page = Main_page.objects.get(pk=1)
    obj_cinema = Cinema.objects.get(pk=cinema_id)
    cinema_gallery = Image.objects.filter(galleryId=obj_cinema.gallery.pk)
    cinema_halls = Hall.objects.filter(cinema=obj_cinema).order_by('name')
    context = {'cinema': obj_cinema,
               'gallery': cinema_gallery,
               'halls': cinema_halls, 'pages': page_list, 'main_page': main_page, 'sessions_today': sessions_today
               }
    return render(request, 'cinema/cinema_card.html', context)


def hall_card(request, hall_id):
    page_list = Other_page.objects.all()
    main_page = Main_page.objects.get(pk=1)
    obj_hall = Hall.objects.get(pk=hall_id)
    hall_sessions = Session.objects.filter(hall=obj_hall)
    hall_gallery = Image.objects.filter(galleryId=obj_hall.gallery.pk)
    context = {'hall': obj_hall,
               'hall_sessions': hall_sessions,
               'gallery': hall_gallery, 'pages': page_list, 'main_page': main_page
               }
    return render(request, 'cinema/hall_card.html', context)


def search(request):
    print(request.POST)
    item_name = request.POST.get('search_text')
    print(item_name)
    if item_name:
        obj_film = Film.objects.filter(name__icontains=item_name)
        if len(obj_film) == 1:
            return redirect('film_card', film_id=obj_film[0].pk)
        else:
            return render(request, 'cinema/search.html', context={'films': obj_film})
    return redirect('kino_cms')
    # obj_promo = News_promo.objects.get(type='Promo', name__contains=item_name)

    # return render(request, '', context={'obj_film': obj_film})
