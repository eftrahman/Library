from django.urls import path
from django.contrib.auth import views as auth_views  # Correct import
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('books/', views.books_list, name='books_list'),
    path('login/',views.loginPage, name='login'),
    path('logout/', views.logoutButton, name='logout'),
]
