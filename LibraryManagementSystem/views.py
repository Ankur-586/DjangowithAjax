from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import *
from django.db.models import Q

def home(request):
    library_card = LibraryCard.objects.all().order_by('-id')
    book = Book.objects.all().order_by('-id')
    student_information = Student_Information.objects.all().order_by('-id')
    borrower = Borrower.objects.all().order_by('-id')
    context = {
        'library_card':library_card,
        'books':book,
        'student_information':student_information,
        'borrower':borrower
    }
    return render(request,'home.html',context)

def borrow_book(request, student_pk, book_pk):
    try:
        borrower = save_borrowed_book(request, student_pk, [book_pk])
        return JsonResponse({'message': 'Borrower created successfully', 'borrower': borrower}, status=201)
    except Exception as e:
        return JsonResponse({'message': f'Failed to borrow book: {str(e)}'}, status=400)

def book_return(request, student_pk, borrow_id):
    if request.method == 'GET':
        late_penalty = late_fine(student_pk,borrow_id)  # Replace with your late_fine function logic
        return JsonResponse({'late_penalty': late_penalty})  # Example response
    # elif request.method == 'POST':
    #     return_date_str = request.POST.get('returnDate')
    #     if not return_date_str:
    #         return HttpResponseBadRequest("Return date is required.")
        
    #     return_date = timezone.datetime.strptime(return_date_str, "%Y-%m-%dT%H:%M")  # Parse the return date string
    #     borrower = Borrower.objects.filter(pk=student_pk, return_date__isnull=True).first()
    #     if borrower:
    #         borrower.return_date = return_date
    #         borrower.save()
    #         late_penalty = late_fine(student_pk,borrow_id)  # Replace with your late_fine function logic
    #         return JsonResponse({'success': True, 'message': 'Return successful', 'late_penalty': late_penalty})
    #     else:
    #         return JsonResponse({'success': False, 'message': 'Borrower not found or book already returned.'})
    # else:
    #     return JsonResponse({'error': 'Invalid request method.'})

def delete(request, id):
  member = Borrower.objects.get(id=id)
  member.delete()
  return JsonResponse({'message':'Record Deleted!!'})
        
# https://www.creative-tim.com/product/soft-ui-dashboard-django

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