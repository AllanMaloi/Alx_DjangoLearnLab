from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import CustomUser

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    # Logic to edit user
    return render(request, 'edit_user.html', {'user': user})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'view_user.html', {'user': user})
