from .models import *
from django import forms
from django.forms import modelformset_factory


class BannerForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'type': 'file', 'class': 'ban-img'}))
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}))

    class Meta:
        model = Banner
        fields = ['image', 'url', 'text']


class BackgroundBannerForm(forms.ModelForm):
    CHOICES = [(True, 'Фото на фон'),
               (False, 'Просто фон')]

    color = forms.CharField(widget=forms.TextInput(attrs={'type': "color",
                                                          'class': "form-control form-control-color"}))
    is_image = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Background_banner
        fields = '__all__'


BannerFormSet = modelformset_factory(model=Banner, form=BannerForm, extra=0, can_delete=True)


class BannerCollectionForm(forms.ModelForm):
    CHOICES = [('5s', '5s'),
               ('10s', '10s'),
               ('15s', '15s')]
    rotation_speed = forms.TimeField(widget=forms.TimeInput())
    # active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Banner_collection
        fields = ['active', 'rotation_speed']
