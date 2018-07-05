from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.github.models import (
    People,
    Repository
)


class PeopleAdmin(admin.ModelAdmin):
    list_display = (
        "get_avatar_tag",
        "name", "login", "type", "bio",
        "location", "html_url", "created_at", "updated_at",
    )
    list_display_links = ["login", ]
    search_fields = ["name", "login"]
    list_filter = ['type', 'alive']
    ordering = ("-updated_at",)

    def get_avatar_tag(self, obj):
        print(obj.avatar)
        return mark_safe('<img width="40" src="{image_url}">'
                         .format(image_url=obj.avatar))

    get_avatar_tag.short_description = 'avatar'


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "html_url",
                    "watchers_count", "stargazers_count", "forks_count", "language",
                    "created_at", "updated_at")
    list_filter = ('state', "language")
    ordering = ("-updated_at",)
    search_fields = ("author", "name", "language",)


admin.site.register(People, PeopleAdmin)
admin.site.register(Repository, RepositoryAdmin)
