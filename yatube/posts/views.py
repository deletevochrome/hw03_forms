# from django.http import HttpResponse
from .forms import PostForm
from django.core.paginator import Paginator
from .models import Post, Group, User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
postsper: int = 10
# Главная страница
# @login_required


def paginator_func(posts, request):
    paginator = Paginator(posts, postsper)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    posts = Post.objects.all()
    page_obj = paginator_func(posts, request)
    return render(request, 'posts/index.html', {'page_obj': page_obj})


# Групповая страница
def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()  # [:POST_COUNT]
    page_obj = paginator_func(posts, request)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    page_obj = paginator_func(posts, request)
    return render(request, 'posts/profile.html', {
        'page_obj': page_obj,
        'author': user,
    })


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    posts = get_object_or_404(Post, id=post_id)  # [:POST_COUNT]
    post_list = Post.objects.select_related('author').filter(
        author=posts.author)
    quantity = post_list.count()
    context = {
        'posts': posts,
        'quantity': quantity,
    }
    return render(request, template, context)


@login_required
def post_create(request):

    form = PostForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'posts/create_post.html', {'form': form})

    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('posts:profile', username=request.user.username)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id
    )
    if request.user != post.author:
        return redirect('posts:post_detail', post_id=post_id)

    form = PostForm(request.POST or None, instance=post)
    if not form.is_valid():
        return render(request, 'posts/create_post.html', {
            'form': form,
            'post_id': post_id,
            'is_edit': True
        })
    form.save()
    return redirect('posts:post_detail', post_id=post_id)
