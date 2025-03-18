from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import your app's views

urlpatterns = [
    # Static test route (Optional; remove if no longer needed)
    path('static-test/', views.static_test, name='static_test'),

    # Registration and Profile views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Login and Logout using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
