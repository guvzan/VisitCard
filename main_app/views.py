from django.shortcuts import render, redirect
from random import randint

from .models import Comment, Post
from .forms import CommentForm

def index(request):
    comments = Comment.objects.filter(status=1).order_by('date_added')
    posts = Post.objects.all()
    post_amount = len(posts)
    comm_amount = len(comments)
    palitra = ['#f6bd60', '#f7ede2', '#f5cac3', '#84a59d',
               '#9AA8A8', '#E0D5BE', '#E0908D', '#F5BB2C',
               '#f28482', '#D2B4AA', '#EDE7F8', '#E99FF4',]
    if comm_amount != 0:
        colors = [palitra[randint(0, comm_amount-1)] for i in range(comm_amount)]
        random_color = palitra[randint(0, comm_amount-1)]
    else:
        colors = []
        random_color = '#f28482'


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
        'post': posts[randint(0, post_amount - 1)]
    }

    return render(request, 'main_app/index.html', context)


