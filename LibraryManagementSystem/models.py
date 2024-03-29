from django.db import models
from django.utils import timezone
from Auth.models import MyUser
import datetime as dt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import random
from django.forms.models import model_to_dict

class LibraryCard(models.Model):
    card_number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.card_number

def generate_library_card(prefix='1nh', branch='is', random_length=3):
    year = str(dt.date.today().year)[2:]
    random_number = ''.join(str(random.randint(0, 9)) for _ in range(random_length))
    library_card_number = f"{prefix}{year}{branch}{random_number}"
    return library_card_number

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Branch(models.Model):
    NO_DEFAULT = 1
    IT = 2
    CS = 3
    ME = 4
    EE = 5
    
    ROLE_CHOICES = (
      (NO_DEFAULT, 'No Default'),
      (IT, 'Information Technology'),
      (CS, 'Computer Science'),
      (ME,'Machenical Engineering'),
      (EE,'Electrical Engineering'),
    )

    branch = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=NO_DEFAULT)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        role_dict = dict(self.ROLE_CHOICES)
        return role_dict.get(self.branch, 'Unknown')
    
    @property 
    def branch_name(self):
        role_dict = dict(self.ROLE_CHOICES)
        return role_dict.get(self.branch, 'Unknown')

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branch'

class Student_Information(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    library_card = models.OneToOneField(LibraryCard, on_delete=models.CASCADE)
    Penalty = models.CharField(max_length=15,default="No Penalty")
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def return_user_email(self):
        return self.branch.user.email
    
    class Meta:
        verbose_name = 'Student_Information'
        verbose_name_plural = 'Student_Information'

class Borrower(models.Model):
    books = models.ManyToManyField(Book)
    book_borrower_student = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def display_book(self):
        return ','.join([str(book) for book in self.books.all()])
    
    def __str__(self):
        return f"PK: {self.pk} - {self.book_borrower_student}"
    
    def get_email(self):
        return self.book_borrower_student.email

    def get_pk_and_student(self):
        return self.pk, str(self.book_borrower_student)

    @property
    def is_overdue(self):
        if self.return_date is None and self.due_date < date.today():
            return True
        return False

    def set_due_date(self):
        self.due_date = self.borrow_date + timedelta(days=10)

def overdue_fine(student_id, borrow_obj_id):
    current_datetime = timezone.localtime(timezone.now())
    borrowing = Borrower.objects.get(id=borrow_obj_id, book_borrower_student=student_id)
    obj_pk, stu_pk = borrowing.get_pk_and_student()

    if borrowing.book_borrower_student != stu_pk:
        return "This borrowing does not belong to the specified student."

    if borrowing.return_date is None and borrowing.due_date < current_datetime:
        due_date_local = timezone.localtime(borrowing.due_date)
        no_of_days = (current_datetime - due_date_local).days
        fine = max(0, no_of_days * 10)  # Add fine for overdue days (minimum 0)
        return fine
    else:
        return 0
    
# def late_fine(student_id, borrow_obj_id):
#     # Here you can implement any additional logic related to calculating late fines.
#     # For now, let's keep it simple and just call overdue_fine.
#     return overdue_fine(student_id, borrow_obj_id)

def save_borrowed_book(request, books_borrowed, borrower_student, borrowers_branch):
    borrow_date = timezone.now()
    due_date = borrow_date + timezone.timedelta(days=10)
    try:
        student = MyUser.objects.get(id=borrower_student)
        branch = Branch.objects.get(id=borrowers_branch)
        borrower = Borrower.objects.create(
            book_borrower_student=student,
            branch=branch,
            borrow_date=borrow_date,
            due_date=due_date
        )
        borrower.books.add(*books_borrowed)
        return JsonResponse({'success': True, 'message': 'Borrower created successfully'})
    except Book.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'One or more books not found'}, status=404)
    except MyUser.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Student not found'}, status=404)
    except Branch.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Branch not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Unexpected error saving borrower: {e}'}, status=500)



# if a book is gettign borrowed frequently then its due date is in 5 days or else 10 days
# return date exceed due date then 10 rupee fine perday
# how to figure out borrow frequency.
# over_due fine column should be present
# limit the no of books student can borrow