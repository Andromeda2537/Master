from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from polls.models import Choice, Question, Author, Book


def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'polls/home.html', context=context)


def polls(request, name_book):
    book = Book.objects.get(name_book=name_book)
    book_id = book.id
    question = Question.objects.get(book=book_id)
    context = {'book': book,
               'question': question}
    return render(request, 'polls/polls.html', context=context)


def choice(request, name_book, book_id):
    question = Question.objects.get(book=book_id)
    context = {'question': question}
    return render(request, 'polls/choice.html', context=context)
