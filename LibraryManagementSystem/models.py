from django.db import models
from django.utils import timezone
from Auth.models import MyUser
import uuid
from django.core.exceptions import ValidationError

class LibraryCard(models.Model):
    card_number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

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

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

class Book_Borrower_Student(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    library_card = models.OneToOneField(LibraryCard, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return self.user.email

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_borrower_student = models.ForeignKey(Book_Borrower_Student, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book_borrower_student.user} borrowed {self.book.title} on {self.loan_date}"
