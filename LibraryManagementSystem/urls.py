from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('',views.home,name='home'),
    
    # search
    path('search_feature/',views.search_feature,name="search_feature"),
    path('get_original_data/',views.get_original_data,name="get_original_data"),
    # other pages
    path('book_return/',views.book_return,name='book_return'),
    
    path('save_borrower/',views.save_borrowed_books,name='save_borrower'),
    path('get_updated_data_for_table/',views.get_updated_data_for_table,name='get_updated_data_for_table'),

    path('get_books/', views.get_books, name='get_books'),
    path('branch/',views.get_branch,name='get_branch'),
    path('get_users_by_branch/', views.get_users_by_branch, name='get_users_by_branch'),
    path('get-authors-for-books/', views.get_authors_for_books, name='get_authors_for_books'),
    
    # Delete data from table
    path('delete/<int:id>', views.delete, name='delete'),
    # Delete Data In Database
    path('del_data/',views.delete_table,name='del_data')
]