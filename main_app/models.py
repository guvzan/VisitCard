from django.db import models

class Comment(models.Model):
    text = models.TextField(max_length=600)
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="", blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    link = models.CharField()

    def __str__(self):
        return self.text[:900] + '...'
