import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

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


@login_required
def post_like(request):
    pk = request.POST.get('pk')
    post = get_object_or_404(Post, pk=pk)
    post.like_toggle(request.user)

    context = {
        'like_count': post.like_users.count(),
    }

    return HttpResponse(json.dumps(context), content_type='application/json')