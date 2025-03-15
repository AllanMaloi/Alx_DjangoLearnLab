from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly

# List all books with optional search functionality
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['author__name']  # Users can search books by author's name

# Retrieve a single book by its ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by its ID.
    Accessible by everyone for read-only access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Add a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to add a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Customize the creation process if needed (e.g., assigning an author)
        serializer.save()  # Adjust as necessary if author assignment is required

# Update an existing book (authenticated users and authors only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users (specific book's author) to update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

# Delete a book (authenticated users and authors only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users (specific book's author) to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]