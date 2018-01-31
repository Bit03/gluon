from django.utils import timezone
from django.db import models
from dapps.models import DApp


# Create your models here.


class Author(models.Model):
    dapp = models.ForeignKey(DApp, related_name='dapp')
    url = models.URLField(max_length=256, default='')
    is_organization = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, related_name='profile')
    name = models.CharField(max_length=64, default='', blank=True)
    bio = models.CharField(max_length=255, default='', blank=True)
    location = models.CharField(max_length=255, default='', blank=True)
    email = models.EmailField(max_length=255, default='', blank=True)
    web_site = models.URLField(max_length=255, default='', blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)


class Repository(models.Model):
    author = models.ForeignKey(Author, related_name='repository')
    url = models.URLField(max_length=256, default='')
    readme = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    def __str__(self):
        return self.url


