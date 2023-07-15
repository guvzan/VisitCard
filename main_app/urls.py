from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    #Головна сторінка
    path('', views.index, name='index'),

    #Адмінка
    path('admin_page', views.admin_page, name='admin_page'),
    path('admin_page/upvote/<int:comment_id>', views.upvote_comment, name='upvote_comment'),
    path('admin_page/downvote/<int:comment_id>', views.downvote_comment, name='downvote_comment'),
    path('admin_page/edit_post/<int:post_id>', views.edit_post, name='edit_post'),
]