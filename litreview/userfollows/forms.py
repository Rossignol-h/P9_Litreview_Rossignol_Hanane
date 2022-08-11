from django import forms


class FollowForm(forms.Form):
    """ Form for subscribe to a user """

    follower = forms.CharField(
                max_length=20,  
                widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"})
                )
