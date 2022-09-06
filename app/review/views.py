from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from multi_form_view import MultiModelFormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import Http404

from review.forms import ReviewForm
from ticket.forms import TicketForm
from review.models import Review
from ticket.models import Ticket

# ======================================================== CREATE REVIEW


# to use "MultiModelFormView" ==> pip install django-multi-form-view six
class CreateReview(LoginRequiredMixin, MultiModelFormView):
    """ View to create a review """

    form_classes = {
        'form_ticket': TicketForm,
        'form_review': ReviewForm,
    }
    template_name = "review/create.html"
    success_url = reverse_lazy('home')
    login_url = 'login'

    def forms_valid(self, forms):
        ticket = forms['form_ticket'].save(commit=False)
        ticket.user = self.request.user
        ticket.has_review = True
        ticket.save()

        review = forms['form_review'].save(commit=False)
        review.user = self.request.user
        review.ticket = ticket
        review.save()

        return super(CreateReview, self).forms_valid(forms)

# ========================================================= EDIT REVIEW


class UpdateReview(LoginRequiredMixin, UpdateView):
    """ View to edit a review """

    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('posts')
    template_name = 'review/update.html'

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            raise Http404
        else :
            return super().form_valid(form)

# ========================================================= RESPONSE TO TICKET


class Response(LoginRequiredMixin, CreateView):
    """ View to reply to a ticket """

    model = Review
    form_class = ReviewForm
    template_name = "review/response_ticket.html"
    success_url = reverse_lazy('home')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = Ticket.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = self.get_context_data()

        form.instance.ticket = context['ticket']
        form.instance.ticket.has_review = True
        form.instance.ticket.save(update_fields=['has_review'])
        return super().form_valid(form)

# ========================================================= DELETE REVIEW


class DeleteReview(LoginRequiredMixin, DeleteView):
    """ View to delete a review """

    model = Review
    success_url = reverse_lazy('posts')
    template_name = 'review/delete.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.ticket.delete()
        return HttpResponseRedirect(success_url)
