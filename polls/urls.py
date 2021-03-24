from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:name_book>/', views.polls, name='content'),
    path('<str:name_book>/<int:book_id>/', views.choice_for_book, name='choice'),
    path('<str:name_book>/<int:book_id>/vote/', views.voting, name='vote')
]