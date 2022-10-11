from django.shortcuts import render
from django.views import View 
# this handles viewing class to handle requests
from django.views.generic.base import TemplateView
# import models
from .models import Post


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class PostList(TemplateView):
    template_name = "post_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context