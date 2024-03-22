from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    # home page
    path('',views.home,name='home'),
    
    # other pages
    path('borrow/<int:student_pk>/<int:book_pk>', views.borrow_book, name='borrow_book'),
    path('fine/<int:student_pk>/<int:borrow_id>/',views.book_return,name='fine'),
    
    path('get_books/', views.get_books, name='get_books'),
    path('get_authors/', views.get_authors, name='get_authors'),
    path('get-users/', views.get_users, name='get_users'),
    path('borrow_book/', views.borrow_book, name='borrow_book'), 
    path('get-authors-for-books/', views.get_authors_for_books, name='get_authors_for_books'),
    # Other Functions
    path('delete/<int:id>', views.delete, name='delete'),

    # test
    path('test',views.test,name='test'),
]