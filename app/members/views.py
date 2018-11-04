from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from members.forms import LoginForm


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


def logout_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)

    return redirect('members:login_view')