from django.contrib import admin
from github.models import Author, AuthorProfile


# Register your models here.

class AuthorProfileStackInlineAdmin(admin.StackedInline):
    model = AuthorProfile


class AuthorAdmin(admin.ModelAdmin):

    inlines = (AuthorProfileStackInlineAdmin, )


admin.site.register(Author, AuthorAdmin)
