from django import forms

from ReviewApp.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('kruti_review', 'khushi_review', 'payu_review', 'other_review')
