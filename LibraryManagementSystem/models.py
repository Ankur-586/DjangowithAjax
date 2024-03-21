from django.db import models
from django.utils import timezone
from Auth.models import MyUser
from datetime import date, timedelta, datetime as dt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import datetime, random
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
    year = str(datetime.date.today().year)[2:]
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

class Student_Information(models.Model):
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

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    library_card = models.OneToOneField(LibraryCard, on_delete=models.CASCADE)
    branch = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=NO_DEFAULT)
    Penalty = models.CharField(max_length=15,default="No Penalty")
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = 'Student_Information'
        verbose_name_plural = 'Student_Information'

class Borrower(models.Model):
    books = models.ManyToManyField(Book)
    book_borrower_student = models.ForeignKey(Student_Information, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def display_book(self):
        return ','.join([str(book) for book in self.books.all()])
    
    def __str__(self):
        return self.display_book
    
    @property
    def is_overdue(self):
        if self.return_date is None and self.due_date < date.today():
            return True
        return False

    def set_due_date(self):
        self.due_date = self.borrow_date + timedelta(days=10)

    def overdue_fine(self,student_pk,borrow_id):
        current_datetime = timezone.localtime(timezone.now())
        borrowing = get_object_or_404(Borrower, id=borrow_id)
        if borrowing.book_borrower_student != student_pk:
            return "This borrowing does not belong to the specified student."
        if borrowing.return_date is None and borrowing.due_date < current_datetime:
            due_date_local = timezone.localtime(borrowing.due_date)
            no_of_days = (current_datetime - due_date_local).days
            fine = max(0, no_of_days * 10)  # Add fine for overdue days (minimum 0)
            return fine
        else:
            return 0
    
def late_fine(student_pk,borrow_id):
    """
    This View Is connected with daj
    """
    student = get_object_or_404(MyUser, pk=student_pk)
    student_info = Student_Information.objects.get(user=student)  # Retrieve Student_Information instance
    borrowings = Borrower.objects.filter(book_borrower_student=student_info) 
    total_fine = 0
    for borrowing in borrowings:
        fine = borrowing.overdue_fine(student_pk,borrow_id)  # Calculate fine for each borrowing
        total_fine += fine
    if total_fine > 0:
        student_info.Penalty = str(total_fine)
        # student_info.save()  # Uncomment this line if you want to update the student's fine in the database
        return total_fine
    else:
        return 'No Fine Amount !!'

def save_borrowed_book(request,student_pk, book_pks):
    """
    Saves a new borrower for the given student and book.
    Args:
        request_data: The dictionary containing form data (if applicable).
        student_pk: The primary key of the student.
        book_pk: The primary key of the book.
    Returns:
        The created borrower object if successful, None otherwise.
    """
    try:
        # Get the student object
        student = get_object_or_404(Student_Information, pk=book_pks)

        # Iterate over each selected book primary key
        for book_pk in book_pks:
            # Get the book object
            book = get_object_or_404(Book, pk=book_pk)

            # Create a borrower object for the current book
            borrower = Borrower(
                book_borrower_student=student,
                book=book,
                borrow_date=timezone.now(),
            )
            borrower.set_due_date()
            borrower.save()

        return JsonResponse({'message': 'Borrowers created successfully!'})
    except (Book.DoesNotExist, Student_Information.DoesNotExist) as e:
        return JsonResponse({'message': 'Book or Student not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': f'Unexpected error saving borrower: {e}'}, status=500)



# if a book is gettign borrowed frequently then its due date is in 5 days or else 10 days
# return date exceed due date then 10 rupee fine perday
# how to figure out borrow frequency.
# over_due fine column should be present
# limit the no of books student can borrow