from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    # Checking what type of request is it?
    # if post then create form object with POST data
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save Valid user to database
            form.save()
            # Get Username what user entered!
            username = form.cleaned_data.get('username')
            # Send flash message
            messages.success(request, f'Hey! {username} Your account has been created! How you can login.')
            # Redirect to home page
            return redirect('login')
    # else create empty form
    else:
        form = UserRegisterForm()
    # Render our registration form
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Hey! Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,

    }
    return render(request, 'users/profile.html', context)
