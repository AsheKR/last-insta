from django.shortcuts import render

from posts.models import Post


def post_list(request):
    posts = Post.objects.filter(author__to_user_relation__from_user=request.user,
                                author__to_user_relation__relation_type='f')
    context = {
        'posts': posts
    }

    return render(request, 'posts/post_list.html', context)