from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('borrow/<int:book_pk>/<int:student_pk>/', views.borrow_book, name='borrow_book'),
]