from django import forms

from ReviewApp.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('harshida_review', 'sarang_review', 'chintan_review', 'other_review')
