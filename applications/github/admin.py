from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.github.models import (
    Organization, People, Repository
)


# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "web_site", "email", "bio", "location", "url", "created_at")
    search_fields = ("name", )


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
        print (obj.avatar)
        return mark_safe('<img width="40" src="{image_url}">'
                         .format(image_url=obj.avatar))
    get_avatar_tag.short_description = 'avatar'


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "html_url",
                    "watch", "star", "fork", "language",
                    "created_at", "updated_at")
    list_filter = ('state', )
    ordering = ("-updated_at",)
    search_fields = ("author", "name", "language", )


# admin.site.register(Organization, OrganizationAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Repository, RepositoryAdmin)
