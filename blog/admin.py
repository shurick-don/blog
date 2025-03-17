from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin


from .models import Post, Category, Tag, Rubric, Image

admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        "tree_actions",
        "indented_title",
    ),
    list_display_links=("indented_title",),
)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    # form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = (
        "id",
        "title",
        "slug",
        "category",
        "created_at",
        "get_photo",
        "views",
    )
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("category", "tags")
    readonly_fields = ("views", "created_at", "get_photo")
    fields = (
        "title",
        "slug",
        "category",
        "tags",
        "content",
        "photo",
        "get_photo",
        "views",
        "created_at",
    )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = "Фото"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# admin.site.register(Rubric)
admin.site.register(Image)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
