from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Book

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')  # Redirect authenticated users
    else:
        if request.method == 'POST':  # POST should be uppercase
            username = request.POST.get('username')  # Use request.POST, not request.post
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)  # Fix typo: `aauthenticate` -> `authenticate`

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username or password is incorrect')  # Fix typo: `messege` -> `messages`

        return render(request, 'books/login.html')

def homepage(request):
    return render(request, 'books/homepage.html')

@login_required
def books_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/books_list.html', context)
