from .models import *
from django import forms
from django.forms import modelformset_factory


class NewsPromoForm(forms.ModelForm):
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    name_ru = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    name_uk = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    description_ru = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    description_uk = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    trailer_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y',
                                                  attrs={'class': "form-control datetimepicker-input",
                                                         'data-target': '#reservationdate'}))
    type = forms.ChoiceField(choices=News_promo_CHOISES)

    class Meta:
        model = News_promo
        fields = '__all__'
        exclude = ['seo', 'gallery', 'name', 'description']


class MainPageForm(forms.ModelForm):
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    phone1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    seo_text_ru = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    seo_text_uk = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    class Meta:
        model = Main_page
        fields = '__all__'
        exclude = ['seo', 'seo_text']


class OtherPageForm(forms.ModelForm):
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    name_ru = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    name_uk = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    description_ru = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    description_uk = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    class Meta:
        model = Other_page
        fields = '__all__'
        exclude = ['seo', 'gallery', 'description', 'name']


class ContactPageForm(forms.ModelForm):
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    name_ru = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    name_uk = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    address_ru = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    address_uk = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    coords = forms.CharField(widget=forms.TextInput(attrs={'class': 'coords form-control'}))

    class Meta:
        model = Contact_page
        fields = '__all__'
        exclude = ['contact_collection', 'name', 'address']


class ContactCollectionForm(forms.ModelForm):
    class Meta:
        model = Contact_collection
        fields = '__all__'
        exclude = ['seo', ]


ContactFormSet = modelformset_factory(Contact_page, form=ContactPageForm, extra=0)
