from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post
 

# This class will list all posts in home (newer on top)
class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html' # This replaces the naming convention of the path <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # Naming the iterable object
    ordering = ['-date_posted']

# Class that renders a detailer blog entry
class PostDetailView(DetailView):
    model = Post
    
# Class to create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form): # The instance of the form will be set to the user that requested in order to validate it
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
    
# Class to edit the a post
class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def test_func(self) -> bool | None: # Prevents that any user edits other people posts.
        post = self.get_object()
        return self.request.user == post.author # Returns a boolean to check


# Class to delete a post
class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self) -> bool | None: 
        post = self.get_object()
        return self.request.user == post.author





def about(request):
    return render(request, 'blog/about.html', {'title':'About'})


