from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from review.models import Review
from ticket.models import Ticket
from itertools import chain

# ======================================================== POSTS MAIN PAGE

class Post(LoginRequiredMixin, ListView):
        """ displays all posts of connected user """

        template_name = "posts/posts.html"
        context_object_name = 'posts'
        login_url = 'login'

        def get_queryset(self):

                tickets = Ticket.objects.filter(user= self.request.user)
                reviews = Review.objects.filter(user= self.request.user)

                posts = sorted(chain(reviews, tickets),
                        key=lambda post: post.time_created,
                        reverse=True)
                return posts
