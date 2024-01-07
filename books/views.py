from django.views.generic import ListView
from .models import Book 

class BookList(ListView):
    model = Book
    template_name = 'books_list.html'

# Create your views here.
