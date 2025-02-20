from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Sample usage
if __name__ == "__main__":
    author_name = "George Orwell"
    library_name = "City Library"

    books_by_author = get_books_by_author(author_name)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(book.title)

    books_in_library = get_books_in_library(library_name)
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(book.title)

    librarian = get_librarian_for_library(library_name)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
