from django.shortcuts import render
from django.views import View 
# this handles viewing class to handle requests
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
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
        name = self.request.GET.get("name")
        if name != None:
            context["posts"] = Post.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["posts"] = Post.objects.all()
            context["header"] = f"Searching for {name}"
        return context

class PostCreate(TemplateView):
    model = Post
    fields = ['name', 'location', 'image', 'currency', 'description', 'highly-recommended']
    template_name = "post_create.html"
    success_irl = "/posts/"
