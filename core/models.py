from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Todo(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    task= models.CharField(max_length=200)
    is_completed= models.BooleanField(default= False)
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task
    
    