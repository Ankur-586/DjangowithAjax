from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from ajax_form.models import contact_us
from django.contrib import messages
import re
from django.core.validators import validate_email
from django.core.exceptions import  ValidationError

def home(request):
    return render(request,'home.html')

def contact_us_page(request):
    return render(request,'contact_us.html')
    
from django.core.exceptions import ValidationError
from django.contrib import messages
# from .forms import ContactForm

def contact_page_form(request):
    if request.method == 'POST':
        # Process form data
        first_name1 = request.POST.get('first_name')
        last_name1 = request.POST.get('last_name')
        email_address = request.POST.get('email_address')            
        website_name = request.POST.get('website_name')
        message1 = request.POST.get('customer_message')
        try:
            validate_email(email_address)
            contact_us(first_name=first_name1, last_name=last_name1, email_address=email_address, website_name=website_name, customer_message=message1).save()
            return JsonResponse({'message': 'Form submitted successfully!'})
        except ValidationError as e:
            error_messages = [str(error) for error in e.messages]
            # messages.error(request, error_messages[0])  # Display first error message
            return JsonResponse({'error': error_messages}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

    
    
# def validate_email_address(request):
#     if request.method == 'POST':
#         email_address = request.POST.get('email_address')
#         if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email_address):
#             print(f"The email address {email_address} is not valid")
#             return False