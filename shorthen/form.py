from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UrlWithAccount, User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateLinkForm(forms.ModelForm):
    class Meta:
        model = UrlWithAccount
        fields = ('id', 'url', 'shorthen_link_id')


class UserUpdateFrom(forms.ModelForm):
    full_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control input_createlink'}),label='Full name', required=False)
    username = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control input_createlink'}),label='User name', required=True)
    email= forms.EmailField(max_length=255,widget= forms.EmailInput(attrs={'class':'form-control input_createlink'}),label='Email', required=True)

    class Meta:
        model = User
        fields = ('id','full_name','username','email')

