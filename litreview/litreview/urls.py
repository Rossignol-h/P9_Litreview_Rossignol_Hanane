from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

# utiliser la vue generique de login
from django.contrib.auth.views import LoginView
from authentication.views import SignUpView, logout_view
from ticket.views import CreateTicket, EditTicket, DeleteTicket
from post.views import Post
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

    # ================================================================ POST

    path('posts/', Post.as_view(), name='posts'),
    path('<int:pk>/edit/', EditTicket.as_view(), name='edit_ticket'),
    path('<int:pk>/delete/', DeleteTicket.as_view(), name='delete_ticket'),

    # ================================================================ USERFOLLOW

    path('follow/', Follow.as_view(), name='follow'),
    path('unfollow/<int:pk>', UnFollow.as_view(), name='unfollow'),
]

# ================================================================ STATIC/MEDIA

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

