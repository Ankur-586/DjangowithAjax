from django.http import HttpResponse, JsonResponse
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

def delete_table(request):
    Student_Information.objects.all().delete()
    return HttpResponse('Deleted')

# def borrow_book(request, student_pk, book_pk):
#     try:
#         borrower = save_borrowed_book(request, student_pk, [book_pk])
#         return JsonResponse({'message': 'Borrower created successfully', 'borrower': borrower}, status=201)
#     except Exception as e:
#         return JsonResponse({'message': f'Failed to borrow book: {str(e)}'}, status=400)

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

# def test(request):
#     return render(request,'LibraryManagementSystem/test-form.html')

def save_borrowed_books(request):
    if request.method == 'POST':
        books_borrowed = request.POST.getlist('books[]')
        borrower_student = request.POST.get('book_borrower_student')
        borrowers_branch = request.POST.get('branch')
        print(books_borrowed, borrower_student, borrowers_branch)
        try:
            # Call the save_borrowed_book function from your models
            save_borrowed_book(request, books_borrowed, borrower_student, borrowers_branch)
            return JsonResponse({'message': 'Borrowed books saved successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def get_updated_data_for_table(request):
    borrowed_books = Borrower.objects.all().order_by('-id')
    data = []
    for borrower in borrowed_books:
        data.append({
            'id': borrower.pk,
            'book_name': ', '.join(book.title for book in borrower.books.all()),
            'author_name': ', '.join(book.author.name for book in borrower.books.all()),
            'book_borrower_student': borrower.book_borrower_student.email,  # Assuming MyUser has an 'email' field
            'student_name': borrower.book_borrower_student.full_name,  # Assuming MyUser has a 'full_name' field
            'branch': borrower.branch.branch_name,  # Assuming Branch has a 'name' field
            'borrow_date': borrower.borrow_date.strftime('%Y-%m-%d %H:%M:%S'),
            'due_date': borrower.due_date.strftime('%Y-%m-%d %H:%M:%S'),
            'return_date': borrower.return_date.strftime('%Y-%m-%d %H:%M:%S') if borrower.return_date else None,
        })
    return JsonResponse(data, safe=False)   

def get_books(request):
    books = Book.objects.all()
    data = [{'id': book.pk, 'text': book.title, 'author_id': book.author.pk} for book in books]
    return JsonResponse({'results': data})

def get_authors_for_books(request):
    book_ids = request.GET.getlist('book_ids[]')
    authors = set()
    for book_id in book_ids:
        book = Book.objects.filter(pk=book_id).first()
        if book:
            authors.add(book.author.pk)
    data = [{'id': author_id, 'text': Author.objects.get(pk=author_id).name} for author_id in authors]
    return JsonResponse({'results': data})

def get_branch(request):
    branches = Branch.objects.all()
    data = [{'id': branch.pk, 'text': str(branch), 'user_id': branch.user.pk} for branch in branches]
    return JsonResponse({'results': data})

def get_users_by_branch(request):
    branch_id = request.GET.get('branch')
    if branch_id:
        users = MyUser.objects.filter(branch__id=branch_id)
        data = [{'id': user.pk, 'email': user.email} for user in users]
        return JsonResponse({'results': data})
    else:
        return JsonResponse({'results': []})

# def borrow_book(request):
#     if request.method == 'POST':
#         # Handle saving of borrowed book here
#         # Example: book_ids = request.POST.getlist('books')
#         return JsonResponse({'message': 'Borrowing successful'}, status=200)
#     return JsonResponse({'error': 'Method not allowed'}, status=405)
        
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