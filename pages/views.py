from django.shortcuts import render, redirect, get_object_or_404
from gallery_seo.forms import ImageFormSet, GalleryForm, SeoForm
from gallery_seo.models import Image
from .forms import NewsPromoForm, MainPageForm, OtherPageForm, ContactPageForm, ContactCollectionForm, ContactFormSet
from .models import News_promo, Other_page, Main_page, Contact_page, Contact_collection
from baners.models import Banner_news, Banner_news_collection
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def news(request):
    news = News_promo.objects.filter(type='News')
    context = {'news': news}
    return render(request, 'pages/news.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def delete_news_promo(request, news_promo_id):
    news_promo = News_promo.objects.get(id=news_promo_id)
    if news_promo.type == 'News':
        news_promo.delete()
        return redirect('news')
    news_promo.delete()
    return redirect('promos')


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def add_news_promo(request, form_type):
    print(form_type)
    if request.method == 'POST':
        news_promo_form = NewsPromoForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST, prefix='seo')
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        print(request.POST, request.FILES)
        if all([seo_form.is_valid(), news_promo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            news_promo = news_promo_form.save(commit=False)
            images = image_form_set.save(commit=False)
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            news_promo.seo = seo
            for image in images:
                if image.image:
                    image.galleryId = gallery
                    image.save()

            news_promo.gallery = gallery
            news_promo.save()
            print(request.POST, request.FILES)
            if form_type == 'News':
                return redirect('news')
            else:
                return redirect('promos')

    else:
        print('not valid')
        news_promo_form = NewsPromoForm(initial={'type': form_type, 'active': True})
        seo_form = SeoForm(prefix='seo')
        image_form_set = ImageFormSet(queryset=Image.objects.none())
    context = {'news_promo_form': news_promo_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'pages/add_news_promo.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def news_promo_update(request, news_promo_id):
    obj = get_object_or_404(News_promo, id=news_promo_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    if request.method == 'POST':
        news_promo_form = NewsPromoForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo, prefix='seo')
        print(request.POST, request.FILES)
        if all([news_promo_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            news_promo = news_promo_form.save(commit=False)
            images = image_form_set.save(commit=False)
            news_promo.seo = seo
            for del_image in image_form_set.deleted_objects:
                print(del_image)
                del_image.delete()
            for image in images:
                if image.image:
                    image.galleryId = news_promo.gallery
                    image.save()
            news_promo.save()
            print(request.POST, request.FILES)
            if news_promo.type == 'News':
                return redirect('news')
            else:
                return redirect('promos')
    else:
        print('no valid')
        image_form_set = ImageFormSet(queryset=gallery_qs)
        news_promo_form = NewsPromoForm(instance=obj)
        seo_form = SeoForm(instance=obj.seo, prefix='seo')

    context = {'news_promo_form': news_promo_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'pages/news_promo_update.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def promos(request):
    obj_promos = News_promo.objects.filter(type='Promo')
    context = {'promos': obj_promos}
    return render(request, 'pages/promos.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def pages(request):
    obj_main_page = Main_page.objects.get(pk=1)
    obl_contact_page = Contact_collection.objects.get(pk=1)
    static_pages = Other_page.objects.filter(pk__lte=5)
    obj_pages = Other_page.objects.filter(pk__gt=5)
    context = {'pages': obj_pages, 'main_page': obj_main_page, 'contact_page': obl_contact_page,
               'static_pages': static_pages}
    return render(request, 'pages/pages.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def add_main_page(request):
    if request.method == 'POST':
        main_page_form = MainPageForm(request.POST)
        seo_form = SeoForm(request.POST, prefix='seo')
        print(request.POST, request.FILES)
        if all([seo_form.is_valid(), main_page_form.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            main_page = main_page_form.save(commit=False)
            main_page.seo = seo
            main_page.save()
            print(request.POST, request.FILES)
            return redirect('pages')
    else:
        print('not valid')
        main_page_form = MainPageForm(initial={'active': True})
        seo_form = SeoForm(prefix='seo')
    context = {'main_page_form': main_page_form, 'seo_form': seo_form}
    return render(request, 'pages/main_page.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def update_main_page(request, main_page_id):
    obj_main_page = get_object_or_404(Main_page, id=main_page_id)
    if request.method == 'POST':
        main_page_form = MainPageForm(request.POST, instance=obj_main_page)
        seo_form = SeoForm(request.POST, instance=obj_main_page.seo, prefix='seo')
        if all([seo_form.is_valid(), main_page_form.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            main_page = main_page_form.save(commit=False)
            main_page.seo = seo
            main_page.save()
            return redirect('pages')
    else:
        print('not valid')
        main_page_form = MainPageForm(instance=obj_main_page)
        seo_form = SeoForm(instance=obj_main_page.seo, prefix='seo')
    context = {'main_page_form': main_page_form, 'seo_form': seo_form}
    return render(request, 'pages/main_page.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def add_page(request):
    if request.method == 'POST':
        other_page_form = OtherPageForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST, prefix='seo')
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        print(request.POST, request.FILES)
        if all([seo_form.is_valid(), other_page_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            other_page = other_page_form.save(commit=False)
            images = image_form_set.save(commit=False)
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            other_page.seo = seo
            for image in images:
                if image.image:
                    image.galleryId = gallery
                    image.save()

            other_page.gallery = gallery
            other_page.save()
            print(request.POST, request.FILES)
            return redirect('pages')
    else:
        print('not valid')
        other_page_form = OtherPageForm()
        seo_form = SeoForm(prefix='seo')
        image_form_set = ImageFormSet(queryset=Image.objects.none())
    context = {'other_page_form': other_page_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'pages/add_update_page.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def update_page(request, page_id):
    obj_page = get_object_or_404(Other_page, id=page_id)
    gallery_qs = Image.objects.filter(galleryId=obj_page.gallery.pk)
    if request.method == 'POST':
        other_page_form = OtherPageForm(request.POST, request.FILES or None, instance=obj_page)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj_page.seo, prefix='seo')
        print(request.POST, request.FILES)
        if all([other_page_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            other_page = other_page_form.save(commit=False)
            images = image_form_set.save(commit=False)
            other_page.seo = seo
            for del_image in image_form_set.deleted_objects:
                print(del_image)
                del_image.delete()
            for image in images:
                if image.image:
                    image.galleryId = other_page.gallery
                    image.save()
            other_page.save()
            print(request.POST, request.FILES)
            return redirect('pages')
    else:
        print('no valid')
        image_form_set = ImageFormSet(queryset=gallery_qs)
        other_page_form = OtherPageForm(instance=obj_page)
        seo_form = SeoForm(instance=obj_page.seo, prefix='seo')

    context = {'other_page_form': other_page_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'pages/add_update_page.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def delete_page(request, page_id):
    del_page = Other_page.objects.get(id=page_id)
    del_page.delete()
    return redirect('pages')


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def contact_page(request):
    obj_collection = get_object_or_404(Contact_collection, id=1)
    contacts_qs = Contact_page.objects.filter(contact_collection_id=1)
    if request.method == 'POST':
        contact_collection_form = ContactCollectionForm(request.POST, instance=obj_collection)
        seo_form = SeoForm(request.POST, instance=obj_collection.seo, prefix='seo')
        contact_formset = ContactFormSet(request.POST, request.FILES or None,
                                         queryset=contacts_qs, initial={'active': True})
        print(request.POST, request.FILES)
        if all([contact_formset.is_valid(), contact_collection_form.is_valid(), seo_form.is_valid()]):
            contact_collection = contact_collection_form.save(commit=False)
            contacts = contact_formset.save(commit=False)
            seo = seo_form.save(commit=False)
            seo.save()
            contact_collection.seo = seo
            contact_collection.save()
            # for del_contact in contact_formset.deleted_objects:
            #     print(del_contact)
            #     del_contact.delete()
            for contact in contacts:
                contact.contact_collection = contact_collection
                contact.save()
            print('Data saved')
            return redirect('pages')
    else:
        print('not valid')
        contact_collection_form = ContactCollectionForm(instance=obj_collection)
        seo_form = SeoForm(instance=obj_collection.seo, prefix='seo')
        contact_formset = ContactFormSet(queryset=contacts_qs, initial={'active': True})
    context = {'contact_collection_form': contact_collection_form,
               'seo_form': seo_form, 'contact_formset': contact_formset}
    return render(request, 'pages/contact_page.html', context)


def site_promos(request):
    obj_promos = News_promo.objects.filter(type='Promo').order_by('date')
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    banners_news = Banner_news.objects.all()
    banners_news_collection = Banner_news_collection.objects.get(pk=1)
    context = {'promos': obj_promos, 'main_page': main_page,
               'banners_news_collection': banners_news_collection, 'banners_news': banners_news, 'pages': page_list}
    return render(request, 'pages/site_promos.html', context)


def news_promo_card(request, news_promo_id):
    news_promo = News_promo.objects.get(pk=news_promo_id)
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    context = {'news_promo': news_promo, 'main_page': main_page, 'pages': page_list}
    return render(request, 'pages/promo_card.html', context)


def site_news(request):
    obj_news = News_promo.objects.filter(type='News').order_by('date')
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    banners_news = Banner_news.objects.all()
    banners_news_collection = Banner_news_collection.objects.get(pk=1)
    context = {'news_list': obj_news, 'main_page': main_page,
               'banners_news_collection': banners_news_collection, 'banners_news': banners_news, 'pages': page_list}
    return render(request, 'pages/site_news.html', context)


def site_other_page(request, page_id):
    page_list = Other_page.objects.all()
    obj_page = page_list.get(pk=page_id)
    main_page = Main_page.objects.get(pk=1)
    gallery = Image.objects.filter(galleryId=obj_page.gallery.pk)
    context = {'page': obj_page, 'main_page': main_page, 'gallery': gallery, 'pages': page_list}
    return render(request, 'pages/site_other_page.html', context)


def site_contact(request):
    contacts = Contact_page.objects.all()
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    banners_news = Banner_news.objects.all()
    banners_news_collection = Banner_news_collection.objects.get(pk=1)
    context = {'contacts': contacts, 'main_page': main_page,
               'banners_news_collection': banners_news_collection, 'banners_news': banners_news, 'pages': page_list}
    return render(request, 'pages/site_contact.html', context)


def site_mobile_app(request):
    main_page = Main_page.objects.get(pk=1)
    page_list = Other_page.objects.all()
    context = {'main_page': main_page, 'pages': page_list}
    return render(request, 'pages/site_mobile_app.html', context)
