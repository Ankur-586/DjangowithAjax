from django.forms import ModelForm
from django import forms
from .models import *

class return_date(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['return_date']
        
        widgets = {
            'return_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Return Date', 'type': 'date'}),
        }