from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Rubric, Category, Image


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

    def get_queryset(self):
        return Post.objects.filter(id__in=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class ThreePostList(ListView):
    model = Post
    template_name = "blog/three_post.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(id__in=[4, 7, 8, 9, 10, 13, 14, 15, 16])


class GalleryPostList(ListView):
    model = Post
    template_name = "blog/gallery_post.html"
    context_object_name = "posts"
    # paginate_by = 9


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


class GalleryByCategoryListView(ListView):
    pass
    # model = Category
    # template_name = "blog/gallery_post.html"
    # context_object_name = "posts"
    # category = None

    # def get_queryset(self):
    #     self.category = Category.objects.get(pk=self.kwargs["pk"])
    #     queryset = Image.obj_img.all().filter(category__id=self.category.id)
    #     return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['rubric'] = self.get_upper(Category.objects.get(pk=self.kwargs['pk']))
    #         return context
