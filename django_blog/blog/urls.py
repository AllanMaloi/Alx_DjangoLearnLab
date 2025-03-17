from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import your blog app views

urlpatterns = [
    # Static test
    path('static-test/', views.static_test, name='static_test'),

    # Authentication views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Registration and Profile views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
