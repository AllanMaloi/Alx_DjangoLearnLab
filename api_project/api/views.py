# api/views.py
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing read-only list view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for handling CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
