from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import SignupForm
from .models import User

# =================================================== SIGNUP CLASS


class SignUpView(SuccessMessageMixin, CreateView):
    """ View for create new user account """

    model = User
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('login')
    success_message = "Votre compte a été créé !"
    form_class = SignupForm

# =================================================== LOGOUT FUNCTION


@login_required
def logout_view(request):
    """ View for log out a connected user """

    logout(request)
    return redirect('login')
