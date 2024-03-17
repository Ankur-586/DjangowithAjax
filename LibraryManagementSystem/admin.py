from django.contrib import admin
from LibraryManagementSystem.models import *

class LibraryCardAdmin(admin.ModelAdmin):
    list_display = ['card_number','issued_date','expiration_date','user','created_at','updated_at']
admin.site.register(LibraryCard,LibraryCardAdmin)

class AuthordAdmin(admin.ModelAdmin):
    list_display = ['name','date_of_birth','nationality','created_at','updated_at']
admin.site.register(Author,AuthordAdmin)

class BookdAdmin(admin.ModelAdmin):
    list_display = ['title','author','publication_year','isbn','quantity','created_at','updated_at']
admin.site.register(Book,BookdAdmin)

class Student_InformationAdmin(admin.ModelAdmin):
    list_display = ['user','library_card','address','Penalty','branch','created_at','updated_at']
admin.site.register(Student_Information,Student_InformationAdmin)

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ['book','book_borrower_student','borrow_date','due_date','return_date','created_at','updated_at']
admin.site.register(Borrower,BorrowerAdmin)