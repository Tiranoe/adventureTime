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