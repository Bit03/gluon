from django.utils import timezone
from django.db import models
from django_extensions.db import fields

from dapps.models import DApp
from caching.base import CachingManager, CachingMixin


# Create your models here.


class Author(models.Model):
    slug = fields.RandomCharField(length=12, unique=True,
                                  include_alpha=False, db_index=True, editable=False)

    dapp = models.ForeignKey(DApp, related_name='dapp')
    url = models.URLField(max_length=256, default='')
    is_organization = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    def __str__(self):
        return self.url


class Organization(CachingMixin, models.Model):
    name = models.CharField(max_length=128, unique=True)
    bio = models.CharField(max_length=255, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, null=True)
    web_site = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=True)

    objects = CachingManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organization")

    @property
    def url(self):
        return "https://github.com/{name}".format(name=self.name)


class People(models.Model):
    dapp = models.ForeignKey(DApp, related_name='people')



class Repository(models.Model):
    author = models.ForeignKey(Author, related_name='repository')
    url = models.URLField(max_length=256, default='')
    readme = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    def __str__(self):
        return self.url
