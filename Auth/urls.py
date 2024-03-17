from django.urls import path
from . import views

urlpatterns = [
    path('reg/',views.reg_user,name='register'),
    path('card/',views.lib_card,name="card"),
]