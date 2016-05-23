from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager (models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating');

class Question (models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    likes = models.ManyToManyField(User)

class Answer (models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
