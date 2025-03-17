from django.urls import path

from .views import *

app_name = "main"

urlpatterns = [
    path("", index, name="general"),
<<<<<<< HEAD
    # path("pint/", pint, name="pint"),
=======
>>>>>>> b0be9c4 (Перенос шаблонов gallery в приложение blog)
]
