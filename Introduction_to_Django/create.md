```python
from bookshelf.models import Book
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
book.save()
# Expected output: Book instance with title '1984', author 'George Orwell', and publication year 1949 created successfully.
```
