from django.contrib import admin
from django.urls import path
from api.views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api app's URLs
]