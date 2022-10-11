from django.shortcuts import render
from django.views import View 
# this handles viewing class to handle requests
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Post:
    def __init__(self, name, location, image, currency, description):
        self.name = name
        self.location = location
        self.image = image
        self.currency = currency
        self.description = description

class PostList(TemplateView):
    template_name = "post_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = posts
        return context