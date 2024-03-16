from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserForm
from .models import User

# add user through on form


def add_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Successfully Added')
            return redirect('display_users')  # Redirect to display_users_view
    else:
        form = UserForm()
    return render(request, 'user_input_form.html', {'form': form})


# Display Users table
def display_users_view(request):
    users = User.objects.all()
    return render(request, 'display_users.html', {'users': users})

# User modifion


def update_user_view(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, f'User Successfully updated')
            # Redirect to display users for updated data
            return redirect('display_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

# Delete User


def delete_user_view(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.error(request, f'User Successfully deleted')
    # Redirect to display users for updated data
    return redirect('display_users')
