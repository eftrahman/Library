from django.urls import path
from django.contrib.auth import views as auth_views  # Correct import
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('books/', views.books_list, name='books_list'),
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
