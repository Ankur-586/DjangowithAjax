from random import choices
from django.forms import ModelForm
from django import forms
from .models import *
from django.utils import timezone
from django.core.validators import validate_email

class AddUser(ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=MyUser.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = MyUser
        fields = ['email','first_name','last_name','date_of_birth']
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email','type':'email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Date of Birth', 'type': 'date'}),
        }
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if validate_email(data):
            raise forms.ValidationError("Enter a Valid Email Address now")
        return data
    
    def clean_Cust_email_id(self):
        data = self.cleaned_data['Cust_email_id']
        if validate_email(data):
            raise forms.ValidationError("Enter a Valid Email Address now")
        return data