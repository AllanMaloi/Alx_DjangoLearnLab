from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITestCase(TestCase):
    def setUp(self):
        """
        Set up the test environment by creating a user, an author, a book, and an authenticated API client.
        """
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )

        # Set up the API client and authenticate the user
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")  # Log in the test user

    # Test creating a new book
    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post("/api/books/create/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    # Test retrieving all books
    def test_get_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # Ensure at least one book is returned

    # Test updating a book
    def test_update_book(self):
        data = {
            "title": "Updated Test Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.put(f"/api/books/update/{self.book.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Test Book")

    # Test deleting a book
    def test_delete_book(self):
        response = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())  # Ensure the book no longer exists

    # Test filtering by author's name
    def test_filter_books_by_author(self):
        response = self.client.get(f"/api/books/?author__name={self.author.name}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", [book["title"] for book in response.data])

    # Test searching by title
    def test_search_books(self):
        response = self.client.get("/api/books/?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", [book["title"] for book in response.data])

    # Test ordering by title
    def test_order_books_by_title(self):
        response = self.client.get("/api/books/?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test permission denial for unauthenticated users
    def test_permission_denied(self):
        self.client.logout()  # Unauthenticate the user
        response = self.client.post("/api/books/create/", {"title": "Forbidden Test"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
