from django.urls import path
from . import views

urlpatterns = [
    path('contatct/',views.contact_us_page,name='contact'),
    path('contatctform/',views.contact_page_form,name='contactform'),
]