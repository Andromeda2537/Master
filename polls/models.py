import datetime
from django.db import models
from django.utils import timezone
# from polls.models import Author, Book, Question, Choice



class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='author', blank=True)
    name_book = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name_book


class Question(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
