from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form

from app.models import Stories


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class StoryForm(forms.ModelForm):
    class Meta:
        model = Stories
        fields = ['title',
        'content',
        'image'
        ]
      

    