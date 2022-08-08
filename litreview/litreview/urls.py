from django.contrib import admin
from django.urls import path

# utiliser la vue generique de login
from django.contrib.auth.views import LoginView
from authentication.views import SignUpView, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),

    # ================================================================ LOGIN-SIGNUP

    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),

]
