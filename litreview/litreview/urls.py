from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

# utiliser la vue generique de login
from django.contrib.auth.views import LoginView
from authentication.views import SignUpView, logout_view
from ticket.views import CreateTicket, EditTicket, DeleteTicket
from review.views import CreateReview, EditReview, DeleteReview, Response
from post.views import Post
from feed.views import Home
from userfollows.views import Follow, UnFollow

urlpatterns = [
    path("admin/", admin.site.urls),

    # ================================================================ LOGIN-SIGNUP

    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),

    # ================================================================ FEED

    path('home/', Home.as_view(), name='home'),
    path('create_ticket/', CreateTicket.as_view(), name='create_ticket'),
    path('create_review/', CreateReview.as_view(), name='create_review'),
    path('response_ticket/<int:pk>/', Response.as_view(), name='response_ticket'),

    # ================================================================ POST

    path('posts/', Post.as_view(), name='posts'),
    path('<int:pk>/edit/', EditTicket.as_view(), name='edit_ticket'),
    path('<int:pk>/delete/', DeleteTicket.as_view(), name='delete_ticket'),
    path('edit_review/<int:pk>/edit/', EditReview.as_view(), name='edit_review'),
    path('delete_review/<int:pk>/delete/', DeleteReview.as_view(), name='delete_review'),


    # ================================================================ USERFOLLOW

    path('follow/', Follow.as_view(), name='follow'),
    path('unfollow/<int:pk>', UnFollow.as_view(), name='unfollow'),
]

# ================================================================ STATIC/MEDIA

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

