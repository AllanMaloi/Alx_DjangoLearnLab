# api/urls.py
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),  # List all books
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a single book
    path('create/', BookCreateView.as_view(), name='book-create'),  # Add a new book
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]
