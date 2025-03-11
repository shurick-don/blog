from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Rubric


class SinglPostList(ListView):
    model = Post
    template_name = "blog/single_post.html"
    context_object_name = "posts"
    paginate_by = 3


class LeftSinglPostList(ListView):
    model = Post
    template_name = "blog/left_single_post.html"
    context_object_name = "posts"
    paginate_by = 3


class ThreePostList(ListView):
    model = Post
    template_name = "blog/three_post.html"
    context_object_name = "posts"
    paginate_by = 9


# def single_post(request):
#     posts = Post.objects.all()
#     return render(request, "blog/single_post.html", {"posts": posts})


# def left_single_post(request):
#     posts = Post.objects.all()
#     return render(request, "blog/left_single_post.html", {"posts": posts})


# def three_post(request):
#     posts = Post.objects.all()
#     return render(request, "blog/three_post.html", {"posts": posts})


class PostList(ListView):
    model = Post
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post


def get_rubric(request):
    pass


class ArticleByCategoryListView(ListView):
    model = Post
    template_name = "blog/single_post.html"
    # template_name = 'blog/Post_by_category.html'
    context_object_name = "posts"
    paginate_by = 3
    category = None

    def get_queryset(self):
        self.category = Rubric.objects.get(pk=self.kwargs["pk"])
        queryset = Post.objects.all().filter(category__pk=self.category.pk)
        return queryset
