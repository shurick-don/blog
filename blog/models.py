from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Rubric(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:rubric", kwargs={"pk": self.pk})

    class MPTTMeta:
        order_insertion_by = ["name"]


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"id": self.id})

    class Meta:
        verbose_name = "Категория(ю)"
        verbose_name_plural = "Категории"
        ordering = ["title"]


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    category = TreeForeignKey(Rubric, on_delete=models.PROTECT)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Статья(ю)"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]


# Загрузка изображений и видео (Gallery)


class Image(models.Model):
    title = models.CharField(
        max_length=100, null=False, verbose_name="Описание изображения"
    )
    image = models.ImageField(
        upload_to="image", verbose_name="Файл с изображением", null=True, blank=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, blank=True
    )

    obj_img = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"id": self.id})


class VideoFile(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name="Описание файла")
    file = models.FileField(
        upload_to="videos", verbose_name="Видеофайл", null=True, blank=True
    )
    obj_video = models.Manager()

    def __str__(self):
        return self.title
