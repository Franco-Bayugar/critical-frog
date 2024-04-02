from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
 

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# This class will list all posts in home (newer on top)
class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html' # I replace the naming convention of the path <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # Naming the iterable object
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
    


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})


