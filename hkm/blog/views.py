from django.shortcuts import render

posts = [
    {
        'author': 'DennisRK',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 15, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 15, 2020'
    }

]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

