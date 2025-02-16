```python
book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
# Expected output: Book title updated to 'Nineteen Eighty-Four'
```
