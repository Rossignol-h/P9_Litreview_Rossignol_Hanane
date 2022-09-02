from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import DeleteView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.db.models import Q

from authentication.models import User
from .models import UserFollows
from .forms import FollowForm

# ================================================================== FOLLOW


class Follow(LoginRequiredMixin, FormView):
    """ View to follow a user """

    model = UserFollows
    login_url = 'login'
    context = {}
    form_class = FollowForm
    template_name = "userfollows/follow.html"
    success_url = reverse_lazy('follow')

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.context['username'] = User.objects.all()
        self.context['follow_user'] = self.model.objects.filter(
            user=self.request.user)
        self.context['followed_by'] = self.model.objects.filter(
            followed_user=self.request.user)
        return self.context

    def form_invalid(self, form):
        """
        If a field is invalid render form and errors.
        """
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        value = form.cleaned_data['follower']
        if value == self.request.user.username:
            form.add_error(None, "Vous ne pouvez pas souscrire à vous même !")
            return self.form_invalid(form)
        try:
            user1 = User.objects.get(username=value.lower())
        except User.DoesNotExist:
            form.add_error(None, "Cet utilisateur n'existe pas !")
            return self.form_invalid(form)

        test2 = self.model.objects.filter(
            Q(followed_user=user1.id) & Q(user=self.request.user)
        )
        if test2:
            form.add_error(None, " Vous suivez déjà cet utilisateur !")
            return self.form_invalid(form)
        else:
            UserFollows.objects.create(user=self.request.user, followed_user=user1)

        return super().form_valid(form)

# ================================================================== UNFOLLOW


class UnFollow(LoginRequiredMixin, DeleteView):
    """ View to unfollow a user """

    model = UserFollows
    template_name = "userfollows/unfollow.html"
    success_url = reverse_lazy('follow')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
