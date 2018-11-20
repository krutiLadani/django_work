from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student,Institute,Branch,Fee

class BrochureForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


class SignUpForm(UserCreationForm):

    COURSE_CHOICES = (
        ('M', 'MBA'),
        ('B', 'B.E.'),
        ('C', 'BCA'),
    )

    contact = forms.CharField(max_length=17)
    enrol_no = forms.CharField(max_length=50)
    institute = forms.ModelChoiceField(queryset=Institute.objects.filter(is_active=True))
    branch = forms.ModelChoiceField(queryset=Branch.objects.filter(is_active=True))
    course = forms.ChoiceField(choices=COURSE_CHOICES)
    birth_date = forms.DateField()


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'contact','enrol_no','institute','branch','course','birth_date')

class FeepaymentForm(forms.ModelForm):

    class Meta:
        model = Fee
        fields = ('amount', 'id',)
