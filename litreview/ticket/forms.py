from django import forms
from . import models


class TicketForm(forms.ModelForm):

    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre', 'label': ''}),
            'description': forms.Textarea(attrs={'rows':10, 'cols':30, 'placeholder': 'Description'}),
        }

class DeleteTicketForm(forms.Form):
    """ Add a hidden filed to delete form """
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)