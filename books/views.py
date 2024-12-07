from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Book

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage') 
    else:
        if request.method == 'POST': 
            username = request.POST.get('username')  
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)  

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username or password is incorrect')  

        return render(request, 'books/login.html')

def logoutButton(request):
    

def homepage(request):
    return render(request, 'books/homepage.html')

@login_required
def books_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/books_list.html', context)
