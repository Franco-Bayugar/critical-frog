from django.db import models

# Imported modules
from django.utils import timezone
from django.contrib.auth.models import User

# Models 
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #no () 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

