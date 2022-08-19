from django import forms
from django.forms import modelformset_factory, inlineformset_factory

from .models import *


class SeoForm(forms.ModelForm):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    keywords = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'row': '5'}))

    class Meta:
        model = SEO
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Image_gallery
        fields = '__all__'


# class AddImageToGallery(forms.ModelForm):
#
#     class Meta:
#         model = Image
#         fields = '__all__'
# class GalleryFormSet(forms.ModelForm):
#     class Meta:
#         model = Image_gallery
#         fields = '__all__'
