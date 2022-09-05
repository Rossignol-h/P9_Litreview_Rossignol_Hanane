from django import forms
from . import models


class TicketForm(forms.ModelForm):
    """ form for create a ticket """

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre', 'label': ''}),
            'description': forms.Textarea(attrs={'rows': 10, 'cols': 30, 'placeholder': 'Description'}),
        }
