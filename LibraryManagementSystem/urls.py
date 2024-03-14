from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('borrow/<int:student_pk>/<int:book_pk>', views.borrow_book, name='borrow_book'),
]