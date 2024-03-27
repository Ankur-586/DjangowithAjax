from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
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

def search_feature(request):
    try:
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            borrowers = Borrower.objects.filter(Q(book_borrower_student__email__icontains=keyword)).order_by('-id')
            data = []
            for borrower in borrowers:
                data.append({
                    'id': borrower.pk,
                    'book_name': ', '.join(book.title for book in borrower.books.all()),
                    'author_name': ', '.join(book.author.name for book in borrower.books.all()),
                    'book_borrower_student': borrower.book_borrower_student.email,
                    'student_name': borrower.book_borrower_student.full_name,
                    'branch': borrower.branch.branch_name,
                    'borrow_date': borrower.borrow_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'due_date': borrower.due_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'return_date': borrower.return_date.strftime('%Y-%m-%d %H:%M:%S') if borrower.return_date else None,
                })
            return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)})

def delete_table(request):
    Student_Information.objects.all().delete()
    return HttpResponse('Deleted')

def book_return(request):
    if request.method == 'GET':
        student_id = request.GET.get("student-id")
        borrow_obj_id = request.GET.get("borrow-id")
        current_datetime = timezone.localtime(timezone.now())
        print(student_id, borrow_obj_id)
        try:
            borrowing = Borrower.objects.get(id=borrow_obj_id, book_borrower_student=student_id)
        except Borrower.DoesNotExist:
            return JsonResponse({'error': "Borrowing not found."}, status=404)

        obj_pk, stu_pk = borrowing.get_pk_and_student()

        if borrowing.book_borrower_student != stu_pk and borrowing.pk != obj_pk:
            return JsonResponse({'error': "This borrowing does not belong to the specified student."})

        if borrowing.return_date is None and borrowing.due_date < current_datetime:
            due_date_local = timezone.localtime(borrowing.due_date)
            no_of_days = (current_datetime - due_date_local).days
            fine = max(0, no_of_days * 10)  # Add fine for overdue days (minimum 0)
            return JsonResponse({'fine': fine})
        else:
            return JsonResponse({'fine': 0, 'return_date': borrowing.return_date})  # No fine

    elif request.method == 'POST':
        return_date_str = request.POST.get('returnDate')
        student_id = request.POST.get("student-id")
        borrow_obj_id = request.POST.get("borrow-id")
        if not return_date_str:
            return JsonResponse({'message': 'Return date is required'})
        return_date = timezone.datetime.strptime(return_date_str, "%Y-%m-%dT%H:%M")

        # Retrieve borrowing instance and update return date if book hasn't been returned yet
        try:
            borrower = Borrower.objects.get(id=borrow_obj_id, book_borrower_student=student_id, return_date__isnull=True)
        except Borrower.DoesNotExist:
            return JsonResponse({'error': 'Borrower not found or book already returned.'}, status=404)

        borrower.return_date = return_date
        borrower.save()
        return JsonResponse({'message': 'Return date updated successfully.', 'return_date': borrower.return_date})

def delete(request, id):
  member = Borrower.objects.get(id=id)
  member.delete()
  return JsonResponse({'message':'Record Deleted!!'})

################### Borrow Book Form  ####################################
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
################### End #################################################
    
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