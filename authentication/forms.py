import re 
from django import forms 
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError 

from .models import CustomUser

User = get_user_model()

# signup form 
class SignupForm(forms.Form):
    email = forms.EmailField(max_length=60, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    password_again = forms.CharField(required=True, widget=forms.PasswordInput)

    # validate email 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        # check email value 
        if not email or email.isspace():
            raise forms.ValidationError('Email is required')
        
        if len(email) < 6 or len(email) > 60:
            raise forms.ValidationError('Email can only be between 6 to 60 characters')
        
        # check if email already exists 
        check_email = User.objects.filter(email__iexact=email)
        if check_email.exists():
            raise forms.ValidationError(f'Email {email} is not available')
        
        return email 
    
    # Validation password 
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_again = cleaned_data.get('password_again')

        if not password or password.isspace():
            self.add_error('password', "Password is required")
        
        if len(password) < 8:
            self.add_error('password', 'Password must be at least 8 characters')
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            self.add_error('password', "Password must contain at least one special character")
        
        if not any(p.islower() for p in password):
            self.add_error('password', 'Password must contain at least one lowercase character')
        
        if not any(p.isupper() for p in password):
            self.add_error('password', 'Password must contain at least one uppercase character')
        
        if not any(p.isdigit() for p in password):
            self.add_error('password', 'Password must contain at least one digit')
        
        if password and password_again and password != password_again:
            self.add_error('password_again', 'Both passwords must match')

        return cleaned_data
        

# login form 
class LoginForm(forms.Form):
    email = forms.EmailField(required=True, max_length=60, min_length=6)
    password = forms.CharField(required=True, widget=forms.PasswordInput)