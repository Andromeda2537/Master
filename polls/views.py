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
    return render(request, 'polls/content_for_voting.html', context=context)


def choice_for_book(request, name_book, book_id):
    question = Question.objects.get(book=book_id)
    book = Book.objects.get(name_book=name_book)
    context = {'book': book,
               'question': question}
    return render(request, 'polls/choice.html', context=context)


def voting(request, name_book, book_id):
    question = Question.objects.get(book_id=book_id)
    answer_options = question.choice_set.get(pk=request.POST['choice'])

    context = {'question': question,
               'answer_options': answer_options}
    answer_options.votes += 1
    answer_options.save()
    return render(request, 'polls/voting_results.html', context=context)




