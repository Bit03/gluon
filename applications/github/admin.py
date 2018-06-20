from django.contrib import admin
from applications.github.models import (
    Organization, People, Repository
)


# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "web_site", "email", "bio", "location", "url", "created_at")
    search_fields = ("name", )


class PeopleAdmin(admin.ModelAdmin):
    list_display = (
        "name", "nickname", "type", "bio",
        "location", "url", "html_url", "created_at"
    )
    search_fields = ["name", "nickname"]
    list_filter = ['type']


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "url",
                    "watch", "star", "fork",
                    "created_at", "updated_at")
    ordering = ("-updated_at",)
    search_fields = ("name", )


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Repository, RepositoryAdmin)
