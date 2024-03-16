from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    # home page
    path('',views.home,name='home'),
    
    # other pages
    path('borrow/<int:student_pk>/<int:book_pk>', views.borrow_book, name='borrow_book'),
    path('fine/<int:student_pk>/',views.book_return,name='fine'),
    
    # Other Functions
    path('delete/<int:id>', views.delete, name='delete'),
]