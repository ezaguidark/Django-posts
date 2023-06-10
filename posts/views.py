from django.shortcuts import render

from django.views.generic import ListView, TemplateView
from .models import Post, Imagen

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'  # en este caso puedes cambiar el nombre de context_object_name

class ImagePageView(ListView):
    model = Imagen
    template_name = 'home.html'
    context_object_name = 'all_images'
