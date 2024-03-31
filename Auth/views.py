from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseServerError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from .models import *
from .forms import *
from django.db import transaction
from LibraryManagementSystem.models import LibraryCard,generate_library_card,Branch
import datetime
# from django.contrib.auth.decorators import permission_required
# from .permissions import FormPermission

def email_login_first_step(request): 
    if request.method == 'POST':
        login_form = EmailForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            print('xyz',email)
            # Perform backend verification of email here
            if MyUser.objects.filter(email=email).exists():
                request.session['login_email'] = email
                return redirect('login_step2')
            else:
                return JsonResponse({'errors': {'email': ['User Does Not exists.']}}, status=400)
    else:
        login_form = EmailForm()
    return render(request, 'Auth/emailform.html', {'login_form': login_form})

def login_step2(request):
    if 'login_email' not in request.session:
        return redirect('email_login_first_step')

    email = request.session['login_email']
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to desired page after successful login
                return redirect('/')
            else:
                # Authentication failed
                form.add_error(None, 'Invalid email or password.')
    else:
        form = PasswordForm()
    return render(request, 'Auth/passwordform.html', {'form': form, 'email': email})

def logout_view(request):
    logout(request)
    return redirect('/')

# @permission_required('view_only',raise_exception=True) 
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
    