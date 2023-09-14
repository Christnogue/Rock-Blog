from collections import UserDict
from django import forms
from .models import Message
from django import forms
from django.contrib.auth.forms import UserCreationForm

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserDict
        fields = ['username', 'password1', 'password2']