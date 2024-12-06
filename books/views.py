from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Book

# Create your views here.

@login_required
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})

from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'books/homepage.html')


def books_list(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/books_list.html', context)
