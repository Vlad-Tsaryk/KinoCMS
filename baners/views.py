from django.shortcuts import render, redirect, get_object_or_404
from .forms import BannerForm, BannerCollectionForm, BackgroundBannerForm, BannerFormSet
from .models import Banner, Banner_collection, Background_banner
from django.forms import modelformset_factory, inlineformset_factory


# Create your views here.
def baners(request):
    obj_banner = get_object_or_404(Banner_collection, id=1)
    obj_back_banner = get_object_or_404(Background_banner, id=1)
    background_banner_form = BackgroundBannerForm(request.POST, request.FILES)
    if request.POST.get('form_type') == 'banners_form':

        print(request.POST, request.FILES)
        banner_formset = BannerFormSet(request.POST, request.FILES,
                                       queryset=Banner.objects.filter(banner_collection_id=1))
        banner_collection_form = BannerCollectionForm(request.POST, instance=obj_banner)
        if all([banner_formset.is_valid(), banner_collection_form.is_valid()]):
            banner_collection = banner_collection_form.save(commit=False)
            banners = banner_formset.save(commit=False)
            for del_banner in banner_formset.deleted_objects:
                print(del_banner)
                del_banner.delete()

            for banner in banners:
                banner.banner_collection = banner_collection
                banner.save()
            print('Data saved')
            return redirect('banners')

        else:
            print('Not valid')

    if request.POST.get('form_type') == 'back_banner_form':
        banner_collection_form = BannerCollectionForm(request.POST, request.FILES, instance=obj_back_banner)
        if banner_collection_form.is_valid():
            banner_collection = banner_collection_form.save(commit=False)
            banner_collection.save()
            return redirect('banners')
        else:
            print('Not valid')

    else:
        print(request.POST)
        background_banner_form = BackgroundBannerForm(instance=obj_back_banner)
        banner_formset = BannerFormSet(queryset=Banner.objects.filter(banner_collection_id=1))
        banner_collection_form = BannerCollectionForm(instance=obj_banner)

    return render(request, 'banners/banner.html', {'banner_collection_form': banner_collection_form,
                                                   'formset': banner_formset,
                                                   'background_banner_form': background_banner_form})
