from django.contrib import admin
from LibraryManagementSystem.models import *

class LibraryCardAdmin(admin.ModelAdmin):
    list_display = ['card_number','issued_date','expiration_date','user']
admin.site.register(LibraryCard,LibraryCardAdmin)

class AuthordAdmin(admin.ModelAdmin):
    list_display = ['name','name','nationality']
admin.site.register(Author,AuthordAdmin)

class BookdAdmin(admin.ModelAdmin):
    list_display = ['title','author','publication_year','isbn']
admin.site.register(Book,BookdAdmin)

class Book_Borrower_StudentAdmin(admin.ModelAdmin):
    list_display = ['user','library_card','address']
admin.site.register(Book_Borrower_Student,Book_Borrower_StudentAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ['book','book_borrower_student','loan_date','return_date']
admin.site.register(Loan,LoanAdmin)