from django.db import models
from django.contrib.auth.models import User

from categories.models import CategoryModel

# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name} : {self.user.username}'
    
    def total_display(self):
        return f"{self.price * self.stock}"