from django.core import validators
from django import forms
from .models import User

class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id','name','email','age','password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'age' : forms.NumberInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }


