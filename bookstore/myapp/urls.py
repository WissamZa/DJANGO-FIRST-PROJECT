from django.urls import path
from . import views

urlpatterns = [
    path('bookstore/', views.get_book, name='bookstore'),
]
