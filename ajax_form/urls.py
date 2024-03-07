from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contatct/',views.contact_us_page,name='contact'),
    path('contatctform/',views.contact_page_form,name='contactform'),
]