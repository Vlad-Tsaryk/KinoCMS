from .models import *
from django import forms
from django.forms import modelformset_factory


class BannerForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'type': 'file', 'class': 'ban-img'}))
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'required': ''}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2', 'required': ''}))

    class Meta:
        model = Banner
        fields = ['image', 'url', 'text']


BannerFormSet = modelformset_factory(model=Banner, form=BannerForm, extra=0, can_delete=True)


class BannerCollectionForm(forms.ModelForm):
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    rotation_speed = forms.ChoiceField(choices=Rotation_Speed_CHOISES,
                                       widget=forms.Select(attrs={'class': 'form-select d-inline',
                                                                  'style': 'width:auto'}))

    class Meta:
        model = Banner_collection
        fields = ['active', 'rotation_speed']


class BackgroundBannerForm(forms.ModelForm):
    CHOICES = [(True, 'Фото на фон'),
               (False, 'Просто фон')]

    color = forms.CharField(widget=forms.TextInput(attrs={'type': "color",
                                                          'class': "form-control form-control-color"}))
    is_image = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={}))

    # is_image = forms.BooleanField
    class Meta:
        model = Background_banner
        fields = '__all__'


class BannerNewsCollectionForm(forms.ModelForm):
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    rotation_speed = forms.ChoiceField(choices=Rotation_Speed_CHOISES,
                                       widget=forms.Select(attrs={'class': 'form-select d-inline',
                                                                  'style': 'width:auto'}))

    class Meta:
        model = Banner_news_collection
        fields = '__all__'


class BannerNewsForm(forms.ModelForm):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'required': ''}))

    class Meta:
        model = Banner_news
        fields = ['image', 'url']


BannerNewsFormSet = modelformset_factory(model=Banner_news, form=BannerNewsForm, extra=0, can_delete=True)
