from django.contrib import admin

from .models import Author, Book, Question, Choice

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Question)
admin.site.register(Choice)
