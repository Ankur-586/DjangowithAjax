from django.shortcuts import render
from .models import *
from .forms import *

def reg_user(request):
    return render(request,'Auth/add_user.html')
