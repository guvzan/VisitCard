from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from random import randint

from .models import Comment, Post
from .forms import CommentForm, PostForm


def index(request):
    comments = Comment.objects.filter(status=1).order_by('date_added')
    posts = Post.objects.all()
    post_amount = len(posts)
    comm_amount = len(comments)
    palitra = ['#f6bd60', '#f7ede2', '#f5cac3', '#84a59d',
               '#9AA8A8', '#E0D5BE', '#E0908D', '#F5BB2C',
               '#f28482', '#D2B4AA', '#EDE7F8', '#E99FF4', ]
    if comm_amount != 0:
        colors = [palitra[randint(0, comm_amount - 1)] for i in range(comm_amount)]
        random_color = palitra[randint(0, comm_amount - 1)]
    else:
        colors = []
        random_color = '#f6bd60'

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.status = 0
            form.save()
        return redirect('main_app:index')

    context = {
        'comm_col': zip(comments, colors),
        'comm_amount': comm_amount,
        'form': form,
        'random_color': random_color,
        'post': posts[randint(0, post_amount - 1)] if post_amount != 0 else 1
    }

    return render(request, 'main_app/index.html', context)


@login_required
def admin_page(request):
    if request.method != 'POST':
        post_form = PostForm()
    else:
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.status = 0
            post_form.save()
        return redirect('main_app:admin_page')

    unseen_comments = Comment.objects.filter(status=0)
    comments = Comment.objects.filter(status__gte=1)
    posts = Post.objects.all()

    context = {
        'post_form': post_form,
        'unseen_comments': unseen_comments,
        'comments': comments,
        'posts': posts,
    }

    return render(request, 'main_app/admin_page.html', context)


@login_required
def upvote_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.status = 1
    comment.save()
    return redirect('main_app:admin_page')


@login_required
def downvote_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.status = 0
    comment.save()
    return redirect('main_app:admin_page')


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:admin_page')

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'main_app/edit_post.html', context)


def pageNotFound(request, exception, template_name='main_app/page404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response
