from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('',views.home,name='home'),
    
    # other pages
    # path('borrow/<int:student_pk>/<int:book_pk>', views.borrow_book, name='borrow_book'),
    path('fine/<int:student_pk>/<int:borrow_id>/',views.book_return,name='fine'),
    
    path('get_books/', views.get_books, name='get_books'),
    # path('get_authors/', views.get_authors, name='get_authors'), 
    # path('borrow_book/', views.borrow_book, name='borrow_book'),  
    path('get-authors-for-books/', views.get_authors_for_books, name='get_authors_for_books'),

    # Other Functions
    path('delete/<int:id>', views.delete, name='delete'),

    # test
    # path('test',views.test,name='test'),
    path('branch/',views.get_branch,name='get_branch'),
    path('get_users_by_branch/', views.get_users_by_branch, name='get_users_by_branch'),
    path('save_borrower/',views.save_borrowed_books,name='save_borrower'),
    path('get_updated_data_for_table/',views.get_updated_data_for_table,name='get_updated_data_for_table'),
    # Delete Data In Database
    path('del_data/',views.delete_table,name='del_data')
]