from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'name', 'about']
        labels = {'text': 'Текст'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 72,
                                          'rows': 4,
                                          'class': 'comment-form-text',
                                          'placeholder': 'Напишіть відгук! Він з\'явиться після перевірки.\n\n'
                                                         'Або залиште відгук на гугл картах, натиснувши на відповідне'
                                                         ' посилання збоку. Він автоматично з\'явиться на сайті.',
                                          'style': 'resize: none;',

                                          }),
            'name': forms.TextInput(attrs={'placeholder': 'Ім\'я та прізвище'}),
            'about': forms.TextInput(attrs={'placeholder': 'Звідки ви?'})}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'title', 'link']
        labels = {'text': 'Текст'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 100,
                                          'rows': 10,
                                          }),
        }
