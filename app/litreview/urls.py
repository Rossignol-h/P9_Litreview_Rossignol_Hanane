from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.urls import path

# utiliser la vue generique de login
from django.contrib.auth.views import LoginView
from authentication.views import SignUpView, logout_view
from review.views import CreateReview, UpdateReview, DeleteReview, Response
from ticket.views import CreateTicket, UpdateTicket, DeleteTicket
from userfollows.views import Follow, UnFollow
from feed.views import Home
from post.views import Post

urlpatterns = [

    path('admin/', admin.site.urls),

    # ================================================================ LOGIN-SIGNUP

    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('avatar/', include('avatar.urls')),
    path('logout/', logout_view, name='logout'),

    # ================================================================ FLUX

    path('home/1', Home.as_view(), name='home1'),
    path('home/', Home.as_view(), name='home'),
    path('create_ticket/', CreateTicket.as_view(), name='create_ticket'),
    path('create_review/', CreateReview.as_view(), name='create_review'),
    path('response_ticket/<int:pk>/', Response.as_view(), name='response_ticket'),

    # ================================================================ POST

    path('posts/', Post.as_view(), name='posts'),
    path('<int:pk>/edit/', UpdateTicket.as_view(), name='edit_ticket'),
    path('<int:pk>/delete/', DeleteTicket.as_view(), name='delete_ticket'),
    path('edit_review/<int:pk>/edit/', UpdateReview.as_view(), name='edit_review'),
    path('delete_review/<int:pk>/delete/', DeleteReview.as_view(), name='delete_review'),

    # ================================================================ USERFOLLOW

    path('follow/', Follow.as_view(), name='follow'),
    path('unfollow/<int:pk>', UnFollow.as_view(), name='unfollow'),
]

# ================================================================ STATIC/MEDIA

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
