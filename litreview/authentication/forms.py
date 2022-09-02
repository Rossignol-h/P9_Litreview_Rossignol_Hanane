from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignupForm(UserCreationForm):
    """ Form to signup a user """

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # fields = ['username', "email","first_name", "last_name",'password1','password2']
        help_texts = {
            'username': None,
            # "email": None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Identifiant'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Mot de passe'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirmation mot de passe'}),
        }
