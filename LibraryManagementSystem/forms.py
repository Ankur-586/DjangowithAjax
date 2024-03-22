from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import *

class AddBorrowerForm(forms.ModelForm):
    """
    Currently This Form Is Not being Used
    """
    class Meta:
        model = Borrower
        fields = ['books','book_borrower_student','borrow_date','due_date','return_date']
        
        widgets = {
            'return_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Return Date', 'type': 'date'}),
        }
        

class return_date(forms.ModelForm):
    """
    Currently This Form Is Not being Used
    """
    class Meta:
        model = Borrower
        fields = ['return_date']
        
        widgets = {
            'return_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Return Date', 'type': 'date'}),
        }
        
# from django_select2.forms import ModelSelect2MultipleWidget
# from .models import Book, MyUser

# class BorrowForm(forms.Form):
#     books = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), widget=ModelSelect2MultipleWidget(model=Book, search_fields=['title__icontains']))
#     user = forms.ModelChoiceField(queryset=MyUser.objects.all(), widget=ModelSelect2Widget(model=MyUser, search_fields=['username__icontains']))
