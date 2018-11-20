import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class LoginForm(AuthenticationForm):
    """
    LoginForm Configs
    """
    username = forms.CharField(label='Username*', max_length=30,
                               widget=forms.TextInput(
                                   attrs={'name': 'username', 'autofocus': 'autofocus'}))
    password = forms.CharField(label="Password*", max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'name': 'password'}))


class RegisterForm(forms.Form):
    """
    RegisterForm Configs
    """
    username = forms.CharField(label='Username*', max_length=30,
                               widget=forms.TextInput(attrs={'name': 'username',
                                                             'autofocus': 'autofocus', 'class': 'validate',
                                                             'pattern': '[A-Za-z\d]{3,15}'}))
    first_name = forms.CharField(label='First Name*', max_length=50,
                                 widget=forms.TextInput(attrs={'name': 'first_name'}))
    last_name = forms.CharField(label='Last Name*', max_length=50,
                                widget=forms.TextInput(attrs={'name': 'last_name'}))
    email = forms.EmailField(label='Email*', max_length=50,
                             widget=forms.EmailInput(attrs={'name': 'email'}))
    password1 = forms.CharField(label='Password*', max_length=30,
                                widget=forms.PasswordInput(attrs={'name': 'password1'}))
    password2 = forms.CharField(label='Confirm Password*', max_length=30,
                                widget=forms.PasswordInput(
                                    attrs={'name': 'password2'}))

    def clean_password1(self):
        """
        validates password
        :return:
        """
        if len(self.cleaned_data['password1']) < 8:
            raise forms.ValidationError('Password must be above 8 characters')
        return self.cleaned_data['password1']

    def clean_password2(self):
        """
        validates confirm password
        :return:
        """
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        """
        Validates username
        :return:
        """
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore. ')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with the specified email address!")
        return email
