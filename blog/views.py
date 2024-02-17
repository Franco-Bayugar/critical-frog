from django.shortcuts import render


posts = [
    {
        'author': 'Franco Bayugar',
        'title': 'Blog Post #1',
        'content': 'Post #1 content',
        'date_posted': '17-Feb-24'
    },
    {
        'author': 'Dbaggio Regal',
        'title': 'Blog Post #2',
        'content': 'Post #2 content',
        'date_posted': '18-Feb-24'
    },
]
    

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
