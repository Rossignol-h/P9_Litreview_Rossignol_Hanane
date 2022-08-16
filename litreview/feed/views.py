from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import CharField, Value
from django.views.generic import ListView
from itertools import chain


class Home(LoginRequiredMixin, ListView):
        """ Displays all tickets and reviews 
        chain and sorted by date on the feed of connected user 
        and users who is following """

        template_name = "flux/home.html"
        context_object_name = 'posts'
        login_url = 'login'

        def get_queryset(self):
            tickets = get_users_viewable_tickets(self.request.user)
            tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

            reviews = get_users_viewable_reviews(self.request.user)
            reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

            posts = sorted(chain(reviews, tickets),
                        key=lambda post: post.time_created,
                        reverse=True)
            page_object = paginate(self.request, posts)

            return page_object


# ==================================================== ALL FUNCTION NEEDED FOR THE CLASS VIEW

from django.core.paginator import Paginator, Page
from django.db.models.query import QuerySet
from django.db.models import Q
from typing import List

from userfollows.models import UserFollows
from authentication.models import User
from review.models import Review
from ticket.models import Ticket


def get_users_subscriptions(user: User) -> List:
    """ retrieves the list of user subscriptions """

    followed_users = UserFollows.objects.filter(user=user)
    subscriptions = [f_user.followed_user for f_user in followed_users]
    return subscriptions


def get_users_viewable_reviews(user: User) -> QuerySet:
    """ displays sorted reviews in the feed """

    subscriptions = get_users_subscriptions(user=user)
    reviews = Review.objects.filter(
        Q(user__in=subscriptions) | Q(user=user) | Q(ticket__user=user)
    )
    return reviews


def get_users_viewable_tickets(user: User) -> QuerySet:
    """ displays sorted tickets in the feed """

    subscriptions = get_users_subscriptions(user=user)
    tickets = Ticket.objects.filter(
        Q(user__in=subscriptions) | Q(user=user)
    )
    return tickets


def paginate(request, object_to_page, item_pet_page: int = 5) -> Page:
    """ returns a Page object allowing to limit the number of this object per page """

    paginator = Paginator(object_to_page, item_pet_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj