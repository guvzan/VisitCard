from django.db import models

class Comment(models.Model):
    text = models.TextField(max_length=600)
    name = models.CharField(max_length=50, default="")
    about = models.CharField(max_length=100, default="", blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.text[:900] + '...'
