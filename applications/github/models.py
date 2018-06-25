from hashlib import md5
from urllib.parse import urlparse

from datetime import datetime, timedelta

from django.db.models import Sum
from django.utils import timezone
from django.db import models
from django_extensions.db import fields
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property
from django_pandas.managers import DataFrameManager
from model_utils import Choices
from taggit.managers import TaggableManager
from caching.base import CachingManager, CachingMixin

from applications.utils.render_md import md


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

    # type = models.IntegerField(choices=TYPE, default=TYPE.user)

    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
    )

    objects = CachingManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organization")

    @property
    def author(self):
        o = urlparse(self.url)
        path_group = o.path.split("/")
        author = path_group[1]
        return author


class People(CachingMixin, models.Model):
    TYPE = Choices(
        (0, 'user', _('user')),
        (1, 'organization', _('organization'))
    )

    name = models.CharField(blank=True, null=True, max_length=128, )
    login = models.CharField(blank=True, max_length=128, unique=True)
    company = models.CharField(blank=True, max_length=128)
    bio = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    blog = models.URLField(max_length=255, blank=True, null=True)

    avatar = models.URLField(max_length=255, blank=True, null=True)

    type = models.IntegerField(choices=TYPE, default=TYPE.user)

    url = models.URLField(max_length=255)
    html_url = models.URLField(max_length=255, default='')
    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = _('users')
        verbose_name_plural = _('user')
        ordering = ("-created_at",)

    def get_watch(self):
        _watchers_count = Repository.objects.filter(author=self.login)\
            .aggregate(watch_sum=Sum('watchers_count'))
        # print (_watchers_count)
        return _watchers_count['watch_sum']
        # return 10

    def get_star(self):
        _stargazers_count = Repository.objects.filter(author=self.login)\
            .aggregate(star_sum=Sum('stargazers_count'))
        return _stargazers_count['star_sum']

    def get_fork(self):
        _forks_count = Repository.objects.filter(author=self.login)\
            .aggregate(fork_sum=Sum('forks_count'))
        return _forks_count['fork_sum']


class Repository(CachingMixin, models.Model):
    author = models.CharField(max_length=128, default='')
    name = models.CharField(max_length=128, default='')
    desc = models.TextField(null=True, blank=True)
    readme = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    html_url = models.URLField(max_length=255, null=True, blank=True)
    homepage = models.URLField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)

    watchers_count = models.IntegerField(default=0)
    stargazers_count = models.IntegerField(default=0)
    forks_count = models.IntegerField(default=0)

    identified_code = models.CharField(null=True, blank=True, max_length=32, unique=True)

    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    updated_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    pushed_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)

    objects = CachingManager()

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = _("repository")
        verbose_name_plural = _("repositories")
        ordering = ("-updated_at",)
        unique_together = ('author', 'name')

    def __str__(self):
        return "{author}/{name}".format(
            author=self.author,
            name=self.name,
        )

    @property
    def full_name(self):
        return "{author}/{repos}".format(
            author=self.author,
            repos=self.name,
        )

    @cached_property
    def last_stats(self):
        return self.stats.last()

    @property
    def watch(self):
        try:
            _watch = self.last_stats.watch
        except Exception:
            _watch = 0
        return _watch

    @property
    def star(self):
        try:
            _star = self.last_stats.star
        except Exception:
            _star = 0
        return _star

    @property
    def fork(self):
        try:
            _fork = self.last_stats.fork
        except Exception:
            _fork = 0
        return _fork

    # @property
    def render_readme(self):
        return md.convert(self.readme)

    def stats_df(self, days=31):
        return self.stats \
            .filter(date__gte=datetime.now() - timedelta(days)) \
            .order_by('date') \
            .to_dataframe(index='date')

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

    objects = DataFrameManager()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return "Watch {watch} / Star {star} / Fork {fork}".format(
            watch=self.watch,
            star=self.star,
            fork=self.fork,
        )


class Commit(models.Model):
    repos = models.ForeignKey(Repository, related_name='commit')
    hash = models.CharField(max_length=128)
    commit_datetime = models.DateField(db_index=True, default=timezone.now)

    def __str__(self):
        return "{s} - {hash}".format(self.repos, self.hash)
