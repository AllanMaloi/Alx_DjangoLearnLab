from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library  # Import Book and Library on separate lines
from django.contrib.auth import views as auth_views
from django.contrib.auth import login  # Added import statement
from .forms import CustomUserCreationForm

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Custom registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
