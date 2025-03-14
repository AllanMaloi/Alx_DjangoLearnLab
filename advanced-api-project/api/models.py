# api/models.py
from django.db import models

class Author(models.Model):
    """
    The Author model represents an author with a name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a book with a title, publication year, and an author.
    A one-to-many relationship is established from Author to Books.
    """
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
