from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('static-test/', views.static_test, name='static_test'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Includes all the URLs from the blog app
path('static/<path:path>/', views.serve_static, name='serve_static'),
]
