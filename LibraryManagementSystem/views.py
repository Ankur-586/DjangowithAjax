from django.shortcuts import render
from .models import *

def home(request):
    library_card = LibraryCard.objects.all()
    book = Book.objects.all()
    book_borrower_student = Book_Borrower_Student.objects.all()
    borrower = Borrower.objects.all()
    context = {
        'library_card':library_card,
        'book':book,
        'book_borrower_student':book_borrower_student,
        'borrower':borrower
    }
    return render(request,'home.html',context)
