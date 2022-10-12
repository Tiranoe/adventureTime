from django.db import models

# Create your models here.
class Post(models.Model):

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=70)
    image = models.CharField(max_length=250)
    currency = models.CharField(max_length=50)
    description = models.TextField(max_length=700)
    highly_recommended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class Attractions(models.Model):

    thingstodo = models.CharField(max_length=150)
    placestovisit = models.CharField(max_length=150)
    userrating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="attractions")

    def __str__(self):
        return self.thingstodo
    def __str__(self):
        return self.placestovisit
