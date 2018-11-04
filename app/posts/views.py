from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from posts.forms import PostCreateForm
from posts.models import Post


@login_required
def post_list(request):
    posts = Post.objects.filter(author__to_user_relation__from_user=request.user,
                                author__to_user_relation__relation_type='f') | Post.objects.filter(author=request.user)
    context = {
        'posts': posts
    }

    return render(request, 'posts/post_list.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(author=request.user)
            return redirect('posts:post_list')
    else:
        form = PostCreateForm()

    context = {
        'form': form
    }

    return render(request, 'posts/post_create.html', context)