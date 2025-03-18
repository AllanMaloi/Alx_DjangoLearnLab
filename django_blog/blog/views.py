from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Custom Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})  # Ensure correct template path

# Profile View (requires login)
@login_required
def profile(request):
    return render(request, 'blog/profile.html')
