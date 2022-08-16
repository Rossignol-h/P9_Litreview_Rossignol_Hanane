from django import forms
from review.models import Review
from ticket.models import Ticket

class EditReviewForm(forms.ModelForm):
    """ Add a hidden filed to edit form """
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Review
        fields = ['headline', 'body', 'rating']


class EditTicketForm(forms.ModelForm):
    """ Add a hidden filed to edit form """

    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

        
class DeleteForm(forms.Form):
    """ Add a hidden filed to delete form """
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)