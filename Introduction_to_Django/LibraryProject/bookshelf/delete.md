```python
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
# Expected output: Book instance deleted successfully
```python
from bookshelf.models import Book

book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
# Expected output: Book instance deleted successfully


3. **Save the file** after making the changes.

### Verify the File

1. **List the files in the `bookshelf` directory** to ensure the `delete.md` file has been updated:
   ```bash
   ls -al

