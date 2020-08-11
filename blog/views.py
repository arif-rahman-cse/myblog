import os
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView, DeleteView,
)

from .models import Post


# Function base view
def home(request):
    print('Home Method')
    if request.GET:
        query = request.GET['q']
        print("Query String: " + str(query))
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# Class base view like listView, DetailsView, UpdateView DeleteView

# Post ListView
class PostListView(ListView):
    model = Post  # Model I want to Covert to List
    template_name = 'blog/home.html'  # Template Name
    context_object_name = 'posts'  # Change default name of objectList
    ordering = ['-date_posted']  # Ordering post LIFO
    paginate_by = 5  # number of page I want to show in single page


class UserPostListView(ListView):
    model = Post  # Model I want to Covert to List
    template_name = 'blog/user_posts.html'  # Template Name
    context_object_name = 'posts'  # Change default name of objectList
    paginate_by = 5  # number of page I want to show in single page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# Post DetailView
class PostDetailView(DetailView):
    model = Post  # Model I want to Covert to List


# Post CreateView
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # Model I want to Work with
    fields = ['title', 'content']  # Fields I want in form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Post UpdateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # Model I want to Work with
    fields = ['title', 'content']  # Fields I want in form

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set Id of Post
        return super().form_valid(form)  # Rerun the form_valid form

    # Only Allow to update user own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Post DeleteView
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  # Model I want to Covert to List
    success_url = '/'

    # Only Allow to update user own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# Search Blog Post
def get_blog_queryset(query=None):
    queryset = []  # Empty List For Storing Search results
    queries = query.split(" ")  # Python Install 2020 = [python, install, 2020]
    for q in queries:
        posts = Post.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))
