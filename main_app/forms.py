from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'first_name', 'last_name']
        labels = {'text': 'Текст'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 70,
                                          'rows': 4,
                                          'placeholder': 'Напишіть відгук! Він з\'явиться після перевірки.',
                                          'style': 'resize: none;',
                                          }),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ім\'я'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Прізвище'})}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'title', 'link']
        labels = {'text': 'Текст'}
