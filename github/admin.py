from django.contrib import admin
from github.models import Author, AuthorProfile


# Register your models here.

class AuthorProfileStackInlineAdmin(admin.StackedInline):
    model = AuthorProfile


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('dapp', 'url', 'is_organization', 'updated_at')
    list_filter = ("is_organization",)

    inlines = (AuthorProfileStackInlineAdmin,)


admin.site.register(Author, AuthorAdmin)
