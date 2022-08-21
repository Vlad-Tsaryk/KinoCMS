from django.shortcuts import render, redirect, get_object_or_404
from gallery_seo.forms import ImageFormSet, GalleryForm, SeoForm
from gallery_seo.models import Image
from .forms import NewsPromoForm
from .models import News_promo


# Create your views here.
def news(request):
    news = News_promo.objects.filter(type='News')
    context = {'news': news}
    return render(request, 'pages/news.html', context)


def delete_news_promo(request, news_promo_id):
    news_promo = News_promo.objects.get(id=news_promo_id)
    if news_promo.type == 'News':
        news_promo.delete()
        return redirect('news')
    news_promo.delete()
    return redirect('promos')


def add_news_promo(request, form_type):
    print(form_type)
    if request.method == 'POST':
        news_promo_form = NewsPromoForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
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
        news_promo_form = NewsPromoForm(initial={'type': form_type})
        seo_form = SeoForm()
        image_form_set = ImageFormSet(queryset=Image.objects.none())
    context = {'news_promo_form': news_promo_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'pages/add_news_promo.html', context)


def news_promo_update(request, news_promo_id):
    obj = get_object_or_404(News_promo, id=news_promo_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    if request.method == 'POST':
        news_promo_form = NewsPromoForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo)
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
        seo_form = SeoForm(instance=obj.seo)

    context = {'news_promo_form': news_promo_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'pages/news_promo_update.html', context)


def promos(request):
    promos = News_promo.objects.filter(type='Promo')
    context = {'promos': promos}
    return render(request, 'pages/promos.html', context)

# def delete_promo(request, promo_id):
#     promo = News_promo.objects.get(id=promo_id)
#     promo.delete()
#     return redirect('promo')
#
#
# def add_promo(request):
#     if request.method == 'POST':
#         promo_form = NewsPromoForm(request.POST, request.FILES)
#         seo_form = SeoForm(request.POST)
#         image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#         print(request.POST, request.FILES)
#         if all([seo_form.is_valid(), promo_form.is_valid(), image_form_set.is_valid()]):
#             seo = seo_form.save(commit=False)
#             seo.save()
#             promo = promo_form.save(commit=False)
#             images = image_form_set.save(commit=False)
#             gallery = GalleryForm().save(commit=False)
#             gallery.save()
#             promo.seo = seo
#             for image in images:
#                 if image.image:
#                     image.galleryId = gallery
#                     image.save()
#
#             promo.gallery = gallery
#             promo.save()
#             print(request.POST, request.FILES)
#             return redirect('promos')
#     else:
#         print('not valid')
#         promo_form = NewsPromoForm()
#         seo_form = SeoForm()
#         image_form_set = ImageFormSet(queryset=Image.objects.none())
#     context = {'promo_form': promo_form, 'images_formset': image_form_set, 'seo_form': seo_form}
#     return render(request, 'pages/add_promo.html', context)
#
#
# def promo_update(request, promo_id):
#     obj = get_object_or_404(News_promo, id=promo_id)
#     gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
#     if request.method == 'POST':
#         promo_form = NewsPromoForm(request.POST, request.FILES or None, instance=obj)
#         image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
#         seo_form = SeoForm(request.POST, instance=obj.seo)
#         print(request.POST, request.FILES)
#         if all([promo_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
#             seo = seo_form.save(commit=False)
#             seo.save()
#             promo = promo_form.save(commit=False)
#             images = image_form_set.save(commit=False)
#             promo.seo = seo
#             for del_image in image_form_set.deleted_objects:
#                 print(del_image)
#                 del_image.delete()
#             for image in images:
#                 if image.image:
#                     image.galleryId = promo.gallery
#                     image.save()
#             promo.save()
#             print(request.POST, request.FILES)
#             return redirect('promos')
#     else:
#         print('no valid')
#         image_form_set = ImageFormSet(queryset=gallery_qs)
#         promo_form = NewsPromoForm(instance=obj)
#         seo_form = SeoForm(instance=obj.seo)
#
#     context = {'promo_form': promo_form, 'images_formset': image_form_set, 'seo_form': seo_form}
#     return render(request, 'pages/promo_update.html', context)
