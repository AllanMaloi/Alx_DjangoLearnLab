from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Fields for filtering
    search_fields = ['title', 'author__name']  # Fields for searching
    ordering_fields = ['title', 'publication_year']  # Fields for sorting
