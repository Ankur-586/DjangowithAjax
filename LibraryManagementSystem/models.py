from django.db import models
from django.utils import timezone
from Auth.models import MyUser
import uuid
from django.core.exceptions import ValidationError
from datetime import date,timedelta,datetime
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class LibraryCard(models.Model):
    card_number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.card_number:  # Generate card number only if not provided
            self.card_number = str(uuid.uuid4())[:20]  # Generate a UUID and truncate to 20 characters
        if not self.card_number:
            raise ValidationError("Please provide a card number.")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.card_number
    

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
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    library_card = models.OneToOneField(LibraryCard, on_delete=models.CASCADE)
    Penalty = models.CharField(max_length=5,default="No Penalty")
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = 'Student_Information'
        verbose_name_plural = 'Student_Information'

class Borrower(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_borrower_student = models.ForeignKey(Student_Information, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Student: {self.book_borrower_student.user} borrowed book: {self.book.title} on Date: {self.borrow_date}"
    
    @property
    def is_overdue(self):
        if self.return_date is None and self.due_date < date.today():
            return True
        return False

    def set_due_date(self):
        self.due_date = self.borrow_date + timedelta(days=10)

    def overdue_fine(self):
        current_datetime = timezone.localtime(timezone.now())
        if self.due_date < current_datetime:
            due_date_local = timezone.localtime(self.due_date)
            no_of_days = (current_datetime - due_date_local).days
            fine = max(0, no_of_days * 10)  # Add fine for overdue days (minimum 0)
            return fine
        return 0  # No fine if the book is not overdue
    
def late_fine(student_pk):
    student = get_object_or_404(MyUser, pk=student_pk)
    student_info = Student_Information.objects.get(user=student)  # Retrieve Student_Information instance
    borrowings = Borrower.objects.filter(book_borrower_student=student_info) 
    print(student, student_info, borrowings)
    total_fine = 0
    for borrowing in borrowings:
        if borrowing.return_date is None:  # Check if book has not been returned yet
            borrowing.return_date = datetime.today()  # Set the return_date to the current datetime
            borrowing.save()  # Save the changes
        fine = borrowing.overdue_fine()  # Pass the student instance
        total_fine += fine
        student_info.Penalty = str(total_fine)
        student_info.save()
        response_data = {"total_fine": total_fine}
        return JsonResponse(response_data)

def save_borrowed_book(request,student_pk, book_pk):
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
    book = get_object_or_404(Book, pk=book_pk)
    student = get_object_or_404(Student_Information, pk=student_pk)
    borrower = Borrower(
        book_borrower_student=student,  # Use the actual field name
        book=book,
        borrow_date=timezone.now(),
    )
    borrower.set_due_date()
    borrower.save()
    return JsonResponse({'message':'Borrower created Successfully!!'})
  except (Book.DoesNotExist, Student_Information.DoesNotExist) as e:
        return JsonResponse({'message': f"Book or Student not found"})
  except Exception as e:
    print(f"Unexpected error saving borrower: {e}")
    return JsonResponse({'message': f"{e}"})

# if a book is gettign borrowed frequently then its due date is in 5 days or else 10 days
# return date exceed due date then 10 rupee fine perday
# how to figure out borrow frequency.
# over_due fine column should be present
# limit the no of books student can borrow