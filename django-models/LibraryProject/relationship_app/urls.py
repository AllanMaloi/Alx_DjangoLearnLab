from django.urls import path
from . import views  # Import views from the current directory
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin_view/', views.admin_view, name='admin_view'),  # Admin view URL
    path('librarian_view/', views.librarian_view, name='librarian_view'),  # Librarian view URL
    path('member_view/', views.member_view, name='member_view'),  # Member view URL
]
