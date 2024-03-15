from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    path('',views.home,name='home'),
    path('borrow/<int:student_pk>/<int:book_pk>', views.borrow_book, name='borrow_book'),
    path('fine/<int:id>/',views.late_fine,name='fine'),
    path('delete/<int:id>', views.delete, name='delete'),
]