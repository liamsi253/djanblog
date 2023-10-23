from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Blog

# Create your views here.


class Home(ListView):
    model = Blog
    template_name = 'index.html'


class Show(DetailView):
    model = Blog
    template_name = 'show.html'


class Add(CreateView):
    model = Blog
    template_name = "add_blog.html"
    fields = '__all__'
