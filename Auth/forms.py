from django.forms import ModelForm
from django import forms
from .models import *
from LibraryManagementSystem.models import Branch
from django.core.validators import validate_email

class AddUser(ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=MyUser.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    branch = forms.ChoiceField(choices=Branch.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = MyUser
        fields = ['email','first_name','last_name','date_of_birth','role','branch']
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email','type':'email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Date of Birth', 'type': 'date'}),
        }
    
    def clean_email_id(self):
        data = self.cleaned_data['email']
        if MyUser.objects.filter(email=data).exists():
            raise forms.ValidationError("User with this Email address already exists!!")
        return data
    
    def clean_password2(self):
        """
        Custom validation to ensure passwords match during registration or password change.
        """
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match. Please try again!!!")
        return password2
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if validate_email(data):
            raise forms.ValidationError("Enter a Valid Email Address now")
        return data
    

         

