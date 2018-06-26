# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from applications.dapps.models import (
    DApp, GitHub, Social, Site,
    EmailAddress, ContractAddress
)


# Register your models here.
class DAppEmailStackInlineAdmin(admin.StackedInline):
    model = EmailAddress


class DappContractAddressStackInlineAdmin(admin.StackedInline):
    model = ContractAddress


class DAppGitHubStackInlineAdmin(admin.StackedInline):
    model = GitHub


class DAppSocialStackInlineAdmin(admin.StackedInline):
    model = Social


class DAppSiteInlineAdmin(admin.StackedInline):
    model = Site


class DAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'status', 'ico_status', "etherian",
                    'tag_list', 'submitted', 'last_update')

    list_filter = ("license", "status", "ico_status")
    search_fields = ("name",)
    exclude = ("is_removed",)
    ordering = ("name", "submitted", "last_update",)

    inlines = [
        DAppEmailStackInlineAdmin,
        DappContractAddressStackInlineAdmin,
        DAppGitHubStackInlineAdmin,
        DAppSocialStackInlineAdmin,
        DAppSiteInlineAdmin,
    ]

    def get_queryset(self, request):
        return super(DAppAdmin, self).get_queryset(request).prefetch_related('tags')

    # def tag_list(self, obj):
    #     return u", ".join(o.name for o in obj.tags.all())


class DAppEmailAdmin(admin.ModelAdmin):
    list_display = ("dapp", "email", "created_at")
    search_fields = ("dapp", "email")


class DAppSiteAdmin(admin.ModelAdmin):
    list_display = ("dapp", "logo", "url", "whitepaper")
    list_display_links = ("url",)
    search_fields = ("dapp",)


class DAppContractAdmin(admin.ModelAdmin):
    pass


class DAppSocialAdmin(admin.ModelAdmin):
    list_display = ("dapp", 'facebook', "medium", "twitter")


class DAppGihubAdmin(admin.ModelAdmin):
    list_display = ("dapp", 'login', 'url', 'html_url', 'updated_at')
    ordering = ("-updated_at", )


admin.site.register(DApp, DAppAdmin)
admin.site.register(GitHub, DAppGihubAdmin)
