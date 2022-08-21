from .models import *
from django import forms


class NewsPromoForm(forms.ModelForm):
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    trailer_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y',
                                                  attrs={'class': "form-control datetimepicker-input",
                                                         'data-target': '#reservationdate'}))
    type = forms.ChoiceField(choices=News_promo_CHOISES)

    class Meta:
        model = News_promo
        fields = '__all__'
        exclude = ['seo', 'gallery']
