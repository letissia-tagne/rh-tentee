from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

User = get_user_model()

class RegisterCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

class RegisterChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username",)
        
        
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'email', 'role']


