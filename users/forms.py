from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import modelformset_factory
from django.utils.safestring import mark_safe

from .models import User, Mail_template


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': "Retype password"}))

    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            # 'first_name', 'last_name', 'birth_date',  'address', 'card_number',
            #       'city', 'gender', 'language', 'phone',
            'email', 'username', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",
                                                             'style': 'width:auto'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email",
                                                            'style': 'width:auto'}))
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': "Password",
                                                                                  'style': 'width:auto'}))
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': "Retype password",
                                                                                  'style': 'width:auto'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "First name",
                                                               'style': 'width:auto'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Last name",
                                                              'style': 'width:auto'}))
    birth_date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y',
                                                        attrs={'class': "form-control datetimepicker-input",
                                                               'data-target': '#reservationdate',
                                                               'style': 'width:20%'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Address",
                                                            'style': 'width:auto'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Card Number",
                                                                'style': 'width:auto'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "City",
                                                         'style': 'width:auto'}))
    gender = forms.ChoiceField(choices=User.CHOISES_gender, widget=forms.RadioSelect()
                               )
    language = forms.ChoiceField(choices=User.CHOISES_language,
                                 widget=forms.RadioSelect())
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'style': 'width:auto'}))

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'birth_date', 'address', 'card_number',
                  'city', 'gender', 'language', 'phone', 'email', 'username', 'password1', 'password2']


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mail_template
        fields = '__all__'


MailingFormSet = modelformset_factory(Mail_template, form=MailingForm, extra=0, can_delete=True)
