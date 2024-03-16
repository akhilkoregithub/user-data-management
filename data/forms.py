from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Day/Month/Year'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'age': 'Age',
            'date_of_birth': 'Date of Birth',
        }
        error_messages = {
            'name': {'required': 'Name is required!'},
            'email': {'required': 'Email is required!'},
            'age': {'required': 'Age is required!'},
            'date_of_birth': {'required': 'Date of Birth is required!'},
        }
