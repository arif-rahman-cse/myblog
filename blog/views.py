from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'Arif Rahman',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 19, 2020'
    },
    {
        'author': 'Abir',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 20, 2020'
    },

    {
        'author': 'Reme',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'July 21, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
