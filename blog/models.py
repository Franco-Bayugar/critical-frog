from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Models 
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #no () 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    # This function will the Django how to find every url of any instance of a post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) # reverse() return the whole url as a string
