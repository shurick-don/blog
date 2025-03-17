from django.shortcuts import render

from blog.models import Post


def index(request):
    return render(request, "main/index.html")
<<<<<<< HEAD


# def pint(request):
#     posts = Post.objects.all()
#     return render(request, "main/pinlist.html", {"posts": posts})
=======
>>>>>>> b0be9c4 (Перенос шаблонов gallery в приложение blog)
