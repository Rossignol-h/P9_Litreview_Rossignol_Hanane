from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.db.models import Q
from itertools import chain
from typing import List

from userfollows.models import UserFollows
from authentication.models import User
from review.models import Review
from ticket.models import Ticket


class Home(LoginRequiredMixin, ListView):
    """ Displays all tickets and reviews
        chain and sorted by date on the feed of connected user
        and users who is following """

    template_name = "feed/home.html"
    context_object_name = 'posts'
    paginate_by = 5
    login_url = 'login'

    def get_queryset(self):
        tickets = get_users_viewable_tickets(self.request.user)
        reviews = get_users_viewable_reviews(self.request.user)

        posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
        return posts

# ============================================== FUNCTIONS


def get_users_subscriptions(user: User) -> List:
    """ retrieves the list of user subscriptions from database """

    followed_users = UserFollows.objects.filter(user=user)
    subscriptions = [f_user.followed_user for f_user in followed_users]
    return subscriptions


def get_users_viewable_reviews(user: User) -> QuerySet:
    """ retrieves the filtered list of reviews from database """

    subscriptions = get_users_subscriptions(user=user)
    reviews = Review.objects.filter(
        Q(user__in=subscriptions) | Q(user=user) | Q(ticket__user=user))
    return reviews


def get_users_viewable_tickets(user: User) -> QuerySet:
    """ retrieves the filtered list of tickets from database """

    subscriptions = get_users_subscriptions(user=user)
    tickets = Ticket.objects.filter(
        Q(user__in=subscriptions) | Q(user=user))
    return tickets
