from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,UpdateView
from testapp1.models import Book

# Create your views here.
class BoookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    fields = ('title','author','pages','price')

class BookUpdateView(UpdateView):
    model = Book
    fields = ('pages','price')