from django.db import models
from dapps.models import DApp


# Create your models here.


class Author(models.Model):
    dapp = models.ForeignKey(DApp, related_name='dapp')
    url = models.URLField(max_length=256, default='')
    is_organization = models.BooleanField(default=False)


class AuthorProfile(models.Model):
    author = models.ForeignKey(Author, related_name='profile')


class Repository(models.Model):
    author = models.ForeignKey(Author, related_name='repository')
    url = models.URLField(max_length=256, default='')
