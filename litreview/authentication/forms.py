from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    """ Form to signup a user """
    
    class Meta:
        model = User
        fields = ['username','password1','password2', 'avatar']
        # fields = ['username', "email","first_name", "last_name",'password1','password2']
        help_texts = {
            'username': None,
            # "email": None,
        }
