from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = "blog"

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("about/", TemplateView.as_view(template_name="blog/about.html"), name="about"),
    path(
        "contact/",
        TemplateView.as_view(
            template_name="blog/contact.html",
            extra_context={"work": "Разработка программного обеспечения"},
        ),
        name="contact",
    ),
    path("single_post/", SinglPostList.as_view(), name="single_post"),
    path("left_post/", LeftSinglPostList.as_view(), name="left_post"),
    path("three_post/", ThreePostList.as_view(), name="three_post"),
    path("gallery_post/", GalleryPostList.as_view(), name="gallery_post"),
    path("<str:slug>/", PostDetailView.as_view(), name="post"),
    path("rubric/<int:pk>", ArticleByCategoryListView.as_view(), name="rubric"),
    path("category/<int:pk>", GalleryByCategoryListView.as_view(), name="category"),
]
