from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

def index(request):
    post = Post.objects.all().first()
    return render(request, 'blog/bootstrap.html', {'post': post})

class PostList(ListView):
    model = Post
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post

