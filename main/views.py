from django.shortcuts import render

from blog.models import Post


def index(request):
    return render(request, "main/index.html")
