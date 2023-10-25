from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = "login.html"
