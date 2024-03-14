from django.http import HttpResponse,HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

def home(request):
    library_card = LibraryCard.objects.all()
    book = Book.objects.all()
    student_information = Student_Information.objects.all()
    borrower = Borrower.objects.all()
    context = {
        'library_card':library_card,
        'books':book,
        'student_information':student_information,
        'borrower':borrower
    }
    return render(request,'home.html',context)

def borrow_book(request, student_pk, book_pk):
    borrower = save_borrowed_book(request, student_pk, book_pk)
    return borrower

# def home(request):{% url 'borrow_book' student_id book_id %}
#     library_card = LibraryCard.objects.all()
#     book = Book.objects.all()
#     student_info = Student_Information.objects.all()
#     borrower = Borrower.objects.all()
#      # Set the number of items per page
#     items_per_page = 1

#     # Paginate each queryset
#     library_card_paginator = Paginator(library_card, items_per_page)
#     book_paginator = Paginator(book, items_per_page)
#     book_borrower_student_paginator = Paginator(student_info, items_per_page)
#     borrower_paginator = Paginator(borrower, items_per_page)

#     # Get the current page number from the request query parameters
#     library_card_page_number = request.GET.get('library_card_page')
#     book_page_number = request.GET.get('book_page')
#     book_borrower_student_page_number = request.GET.get('book_borrower_student_page')
#     borrower_page_number = request.GET.get('borrower_page')

#     # Get the corresponding page objects for each table
#     library_card_page_obj = library_card_paginator.get_page(library_card_page_number)
#     book_page_obj = book_paginator.get_page(book_page_number)
#     book_borrower_student_page_obj = book_borrower_student_paginator.get_page(book_borrower_student_page_number)
#     borrower_page_obj = borrower_paginator.get_page(borrower_page_number)

#     context = {
#         'library_card': library_card_page_obj,
#         'book': book_page_obj,
#         'book_borrower_student': book_borrower_student_page_obj,
#         'borrower': borrower_page_obj
#     }
#     return render(request, 'home.html', context)