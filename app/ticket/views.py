from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404

from .forms import TicketForm
from .models import Ticket

# ========================================================= CREATE TICKET


class CreateTicket(LoginRequiredMixin, generic.CreateView):
    """ View to create a ticket """

    model = Ticket
    success_url = reverse_lazy('home')
    template_name = 'ticket/create.html'
    form_class = TicketForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# ========================================================= EDIT TICKET


class UpdateTicket(LoginRequiredMixin, UpdateView):
    """ View to edit a ticket """

    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy('posts')
    template_name = 'ticket/update.html'

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            raise Http404
        else :
            return super().form_valid(form)

# ========================================================= DELETE TICKET


class DeleteTicket(LoginRequiredMixin, DeleteView):
    """ View to delete a ticket """

    model = Ticket
    success_url = reverse_lazy('posts')
    template_name = 'ticket/delete.html'

    def form_valid(self, form):

            if self.object.user != self.request.user:
                raise Http404
            else :
                success_url = self.get_success_url()
                self.object.delete()
                return HttpResponseRedirect(success_url)