from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',  'email',
                  'password1', 'password2',
                  'first_name', 'last_name',
                  )
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "w-3/4 py-1 px-4 rounded"
        
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Your Email Address",
        "class": "w-3/4 py-3 px-5 rounded"
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your Password",
        "class": "w-3/4 py-2 px-4 rounded"
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your Password",
        "class": "w-3/4 py-2 px-4 rounded"
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "First Name",
        "class": "w-3/4 py-2 px-4 rounded"
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Last Name",
        "class": "w-3/4 py-2 px-4 rounded"
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': "w-3/4 py-4 px-6 rounded"
    }))
        
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': "w-3/4 py-4 px-6 rounded"
    }))
