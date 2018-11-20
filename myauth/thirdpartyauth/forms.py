from django import forms
from django.core.validators import RegexValidator


class UserAuth(forms.Form):

    user_name = forms.CharField(label='Username', max_length=50)
    pswd = forms.CharField(label='Password', max_length=10)