from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    CHOICES = [
        (1,""), (2,""), (3,""), (4,""), (5,"")
    ]
    rating = forms.ChoiceField(label=" Note ", widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Review
        exclude = ('time_created',)
        fields = ['headline', 'body', 'rating']
        widgets = {
            'headline': forms.TextInput(attrs={'placeholder': 'Titre', 'label': ''}),
            'body': forms.Textarea(attrs={'rows':10, 'cols':30, 'placeholder': 'Commentaires'}),
        }