from rest_framework import generics
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters  # Correct import for django-filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly
class BookListView(generics.ListAPIView):
    """
    Retrieve all books with support for filtering, searching, and ordering.

    Filtering:
    - Filter by title, author's name, and publication year using query parameters (e.g., /books/?title=Django).

    Searching:
    - Search for books by title or author's name using 'search' query parameter (e.g., /books/?search=Advanced).

    Ordering:
    - Order results by title or publication year using 'ordering' query parameter (e.g., /books/?ordering=-publication_year).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # Add OrderingFilter here
    filterset_fields = ['title', 'author__name', 'publication_year']  # Define fields for filtering
    search_fields = ['title', 'author__name']  # Define fields for searching
    ordering_fields = ['title', 'publication_year']  # Define fields for sorting
