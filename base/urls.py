from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from main.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    path("", include("main.urls", namespace="main")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
