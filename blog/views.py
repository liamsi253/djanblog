from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Blog
from .forms import BlogForm
# Create your views here.


class Home(ListView):
    model = Blog
    template_name = 'index.html'


class Show(DetailView):
    model = Blog
    template_name = 'show.html'


class Add(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "add_blog.html"
    # fields = '__all__'


class Edit(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "edit_blog.html"


class Delete(DeleteView):
    model = Blog
    template_name = "delete_blog.html"
    success_url = reverse_lazy('home')
