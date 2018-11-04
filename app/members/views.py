from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from members.forms import LoginForm, ProfileForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.user
            if user is not None:
                login(request, user)
                return redirect('posts:post_list')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'members/login.html', context)


@login_required
def logout_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)

    return redirect('members:login_view')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()

    form = ProfileForm(instance=request.user)
    return render(request, 'members/profile.html', context={'form': form})
