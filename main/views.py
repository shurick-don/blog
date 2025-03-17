from django.shortcuts import render

from blog.models import Post


def index(request):
    return render(request, "main/index.html")


# def pint(request):
#     posts = Post.objects.all()
#     return render(request, "main/pinlist.html", {"posts": posts})
