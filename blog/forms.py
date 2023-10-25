from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'body')

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
