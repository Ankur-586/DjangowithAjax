from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .models import *
from .forms import *

# def reg_user(request):
#     if request.method == 'POST':
#         form = AddUser(request.POST)
#         if form.is_valid():
#             try:
#                 user = form.save(commit=False)
#                 user.password = make_password(form.cleaned_data['password1'])
#                 user.save()
#                 return JsonResponse({'message': 'Registration successful!'})
#             except IntegrityError as e:
#                 if 'UNIQUE constraint' in str(e):  # More specific error handling
#                     return JsonResponse({'error': 'Username already exists.'}, status=400)
#                 else:
#                     return JsonResponse({'error': 'Database error occurred.'}, status=400)
#             except Exception as e:
#                 # Log the exception for debugging
#                 print(f"Registration error: {e}")
#                 return HttpResponseServerError('Internal server error.')
#         else:
#             # Extract form errors with more descriptive messages
#             form_errors = {field: form.errors[field] for field in form.errors}
#             return JsonResponse({'errors': form_errors}, status=400)
#     else:
#         form = AddUser()
#     return render(request, 'Auth/add_user.html', {'form': form})

def reg_user(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data['password1'])
                user.save()
                return JsonResponse({'message': 'Registration successful!'})
            except IntegrityError:
                return JsonResponse({'errors': {'email': ['Username already exists.']}}, status=400)
            except Exception as e:
                print(f"Registration error: {e}")
                return HttpResponseServerError('Internal server error.')
        else:
            # Extract form errors with more descriptive messages
            form_errors = {field: form.errors[field] for field in form.errors}
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = AddUser(initial={"email": None})
    return render(request, 'Auth/add_user.html', {'form': form})

