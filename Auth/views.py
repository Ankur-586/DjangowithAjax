from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .models import *
from .forms import *

def reg_user(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)  # Don't commit yet
                user.password = make_password(form.cleaned_data['password1'])  # Hash password
                user.save()
                return JsonResponse({'message': 'Form submitted successfully!'})
            except IntegrityError as e:
                return JsonResponse({'IntegrityError': str(e)}, status=400)
            except Exception as e:
                return JsonResponse({'Exception': str(e)}, status=500) # Internal server error
        else:
            # Form is invalid, return form errors
            form_errors = {field: errors[0] for field, errors in form.errors.items()}
            return JsonResponse({'formfielderror': form_errors}, status=400)
    form = AddUser()
    return render(request, 'Auth/add_user.html', {'form': form})

# def reg_user(request):
#     if request.method == 'POST':
#         form = AddUser(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message': 'Form submitted successfully!'})
#     form = AddUser()
#     return render(request, 'Auth/add_user.html', {'form': form})

