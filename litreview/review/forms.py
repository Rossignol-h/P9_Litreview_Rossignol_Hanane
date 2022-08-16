from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    CHOICES = [
        (0, " ★0"), (1, " ★1"), (2, " ★2"), (3, " ★3"), (4, " ★4"), (5, " ★5")
    ]
    rating = forms.ChoiceField(label=" Note ", widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Review
        exclude = ('time_created',)
        fields = ['headline', 'body', 'rating']

class DeleteReviewForm(forms.Form):
    """ Add a hidden filed to delete form """
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
