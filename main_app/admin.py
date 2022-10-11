from django.contrib import admin
from .models import Post # import the Artist model from models.py
# Register your models here.

admin.site.register(Post) # this line will add the model to the admin panel