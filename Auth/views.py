from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseServerError
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .models import *
from .forms import *
from django.db import transaction
from LibraryManagementSystem.models import LibraryCard, Student_Information,generate_library_card,Branch
import datetime

def reg_user(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save(commit=False)
                    user.password = make_password(form.cleaned_data['password1'])
                    user.save()
                    lib_card(user)
                    # Save branch for the user
                    if user.role != MyUser.is_admin:
                        branch_value = form.cleaned_data.get('branch')
                        if branch_value:
                            branch = Branch.objects.create(branch=branch_value, user=user)
                            branch.save()
                return JsonResponse({'message': 'Registration successful!'})
            except IntegrityError:
                return JsonResponse({'errors': {'email': ['Username already exists.']}}, status=400)
            except Exception as e:
                print(f"Registration error: {e}")
                return HttpResponseServerError('Internal server error.')
        else:
            # Extract form errors with more descriptive messages
            form_errors = {field: form.errors[field] for field in form.errors}
            return JsonResponse({'errors': form_errors}, status=400)
    else:
        form = AddUser()
    return render(request, 'Auth/add_user.html', {'form': form})

def lib_card(user):
    try:
        library_card = LibraryCard(
            card_number=generate_library_card(),
            issued_date=datetime.date.today(),  # Call today() method to get current date
            expiration_date=datetime.date.today() + datetime.timedelta(days=365*4),
            user=user,
        )
        library_card.save()
    except Exception as e:
        # print(f"Library card creation error: {e}")
        raise e 
    