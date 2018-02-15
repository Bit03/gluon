from hashlib import md5
from django.utils import timezone
from django.db import models
from django_extensions.db import fields
from django.utils.translation import ugettext_lazy as _
# from dapps.models import DApp
from caching.base import CachingManager, CachingMixin
from django_pandas.managers import DataFrameManager
from taggit.managers import TaggableManager


class Organization(CachingMixin, models.Model):
    slug = fields.RandomCharField(length=12, unique=True,
                                  include_alpha=False, db_index=True, editable=False)
    name = models.CharField(max_length=128)
    bio = models.CharField(max_length=255, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, null=True)
    web_site = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    avatar = models.URLField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255, unique=True, default='')

    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)

    objects = CachingManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organization")

    # @property
    # def url(self):
    #     return "https://github.com/{name}".format(name=self.name)


class People(CachingMixin, models.Model):
    name = models.CharField(blank=True, null=True, max_length=128, )
    nickname = models.CharField(blank=True, max_length=128)
    bio = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    web_site = models.URLField(max_length=255, blank=True, null=True)

    avatar = models.URLField(max_length=255, blank=True, null=True)

    url = models.URLField(max_length=255, unique=True, default='')
    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = _('people')
        verbose_name_plural = _('people')
        ordering = ("-created_at",)


class Repository(CachingMixin, models.Model):
    author = models.CharField(max_length=128, default='')
    name = models.CharField(max_length=128, default='')
    desc = models.TextField(null=True, blank=True)
    readme = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)

    identified_code = models.CharField(null=True, blank=True, max_length=32, unique=True)

    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    objects = CachingManager()

    tags = TaggableManager()

    class Meta:
        verbose_name = _("repository")
        verbose_name_plural = _("repositories")

    def __str__(self):
        return "{author}/{name}".format(
            author=self.author,
            name=self.name,
        )

    def save(self, *args, **kwargs):
        if self.identified_code is None:
            self.identified_code = md5(self.url.encode('utf-8')).hexdigest()
        super(Repository, self).save(*args, **kwargs)


class RepositoryStats(CachingMixin, models.Model):
    repos = models.ForeignKey(Repository, related_name='stats')
    watch = models.PositiveIntegerField(default=0)
    star = models.PositiveIntegerField(default=0)
    fork = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True, editable=False)
    # datetime = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    # date = models.DateField(auto_created=True, db_index=True, editable=False)

    objects = DataFrameManager()

    class Meta:
        ordering = ('-date', )

    def __str__(self):
        return "Watch {watch} / Star {star} / Fork {fork}".format(
            watch=self.watch,
            star=self.star,
            fork=self.fork,
        )
