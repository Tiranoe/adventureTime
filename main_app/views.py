from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse
# this handles viewing class to handle requests
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
# import models
from .models import Post, Attractions
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


@method_decorator(login_required, name='dispatch')
class PostList(TemplateView):
    template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["posts"] = Post.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["posts"] = Post.objects.filter(user=self.request.user)
            context["header"] = f"Searching for {name}"
        return context


class PostCreate(CreateView):
    model = Post
    fields = ['name', 'location', 'image', 'currency', 'description', 'highly_recommended']
    template_name = "post_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
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


class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
    success_url = "/posts/"


class AttractionCreate(View):
    def post(self, request, pk):
        thingstodo = request.POST.get("thingstodo")
        placestovisit = request.POST.get("placestovisit")
        userrating = request.POST.get("userrating")
        post = Post.objects.get(pk=pk)
        Attractions.objects.create(thingstodo=thingstodo, placestovisit=placestovisit, userrating=userrating, post=post)
        return redirect('post_detail', pk=pk)


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
