from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
