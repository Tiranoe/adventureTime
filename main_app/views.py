from django.shortcuts import render
from django.urls import reverse
# this handles viewing class to handle requests
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
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

class PostCreate(CreateView):
    model = Post
    fields = ['name', 'location', 'image', 'currency', 'description', 'highly_recommended']
    template_name = "post_create.html"
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostUpdate(UpdateView):
    model = Post
    fields = ['name', 'location', 'image', 'currency', 'description', 'highly_recommended']
    template_name = "post_update.html"
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})