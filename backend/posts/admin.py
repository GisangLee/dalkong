from django.contrib import admin
from . import models as post_models

# Register your models here.


class PhotoInline(admin.TabularInline):
    model = post_models.Photo


@admin.register(post_models.Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "author",
        "title",
        "desc",
    )

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "게시글 기본 정보",
            {
                "fields": (
                    "author",
                    "title",
                    "desc",
                ),
            },
        ),
        (
            "태그 정보",
            {
                "fields": ("tags",),
            },
        ),
    )

    filter_horizontal = ("tags",)