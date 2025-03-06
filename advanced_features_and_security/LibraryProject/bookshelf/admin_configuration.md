# Django Admin Configuration for Book Model

## Registering the Book Model

In `bookshelf/admin.py`, register the `Book` model to enable admin functionalities for it:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
