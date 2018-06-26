# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from urllib.parse import urlparse

from django.core import urlresolvers
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django_extensions.db import fields
from model_utils.models import SoftDeletableModel
from model_utils.fields import StatusField
from model_utils import Choices
from taggit.managers import TaggableManager

from applications.github.models import Repository


class DApp(SoftDeletableModel):
    # Platform = Choices("")
    ICO_STATUS_CHOICES = Choices("Planned", "Active", "Complate")
    STATUS = Choices("demo", "live", "concept", "wip")
    LICENSE_CHOICES = Choices("MIT", "GPLv3", "Apache License 2.0", "proprietary", "GPL")

    slug = fields.RandomCharField(length=12, unique=True,
                                  include_alpha=False, db_index=True, editable=False)
    name = models.CharField(max_length=64, )
    platform = models.CharField(max_length=64, )
    symbol = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, default='', )
    description_cn = models.TextField(blank=True, default='')
    country_of_origin = models.CharField(max_length=64, default='', blank=True)

    faq = models.CharField(max_length=255, default='')
    founder = models.CharField(max_length=255, default='', blank=True)
    vc = models.CharField(max_length=255, default='', blank=True, )
    etherian = models.CharField(max_length=255, default='', blank=True)

    license = StatusField(choices_name='LICENSE_CHOICES', null=True, blank=True, default=None)
    status = StatusField(choices_name='STATUS', null=True, blank=True)
    ico_status = StatusField(choices_name='ICO_STATUS_CHOICES', null=True, blank=True, default=None)

    submitted = models.DateTimeField(null=True, blank=True, db_index=True)
    last_update = models.DateTimeField(null=True, blank=True, db_index=True)

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = "Decentralised Applications"
        verbose_name_plural = "Decentralised Applications"
        ordering = ("last_update",)

    def __str__(self):
        return self.name

    @property
    def tag_list(self):
        return u", ".join(o.name for o in self.tags.all())

    def get_absolute_url(self):
        return urlresolvers.reverse('dapps:detail', args=[self.slug, ])


class ContractAddress(models.Model):
    dapp = models.OneToOneField(DApp, related_name='contract')
    mainnet = models.CharField(max_length=128, null=True, blank=True)
    ropsten = models.CharField(max_length=128, null=True, blank=True)
    kovan = models.CharField(max_length=128, null=True, blank=True)
    rinkeby = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = 'Contract Address'
        verbose_name_plural = 'Contract Address'

    def __str__(self):
        return self.mainnet


class EmailAddress(models.Model):
    dapp = models.OneToOneField(DApp, related_name='email')
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)

    class Meta:
        verbose_name = "Email Address"

    def __str__(self):
        return self.email


class Site(models.Model):
    dapp = models.OneToOneField(DApp, related_name='site')
    logo = models.URLField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, )
    whitepaper = models.URLField(max_length=1024, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Site"

    def __str__(self):
        return self.url

    @property
    def logo_url(self):
        if len(self.logo) > 0:
            return self.logo
        else:
            return self.dapp.github.avatar_url


class GitHub(models.Model):
    dapp = models.OneToOneField(DApp, related_name='github')
    login = models.CharField(max_length=64, default='')
    avatar_url = models.URLField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255)
    html_url = models.URLField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    blog = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    def __str__(self):
        return self.url

    @property
    def author(self):
        if "github.com" in self.url:
            o = urlparse(self.url)
            path_group = o.path.split("/")
            author = path_group[1]
            return author
        return None

    def get_watch(self):
        _watchers_count = Repository.objects.filter(author=self.login) \
            .aggregate(watch_sum=Sum('watchers_count'))
        return _watchers_count['watch_sum'] if _watchers_count['watch_sum'] else 0

    def get_star(self):
        _stargazers_count = Repository.objects.filter(author=self.login) \
            .aggregate(star_sum=Sum('stargazers_count'))
        return _stargazers_count['star_sum'] if _stargazers_count['star_sum'] else 0

    def get_fork(self):
        _forks_count = Repository.objects.filter(author=self.login) \
            .aggregate(fork_sum=Sum('forks_count'))
        return _forks_count['fork_sum'] if _forks_count['fork_sum'] else 0

    def get_repos_count(self):
        repos_count = Repository.objects.filter(author=self.login).count()
        return repos_count


class Social(models.Model):
    dapp = models.OneToOneField(DApp, related_name='social')
    reddit = models.URLField(max_length=255, default='', blank=True)
    slack = models.URLField(max_length=255, default='', blank=True)
    gitter = models.URLField(max_length=255, default='', blank=True)
    blog = models.URLField(max_length=255, default='', blank=True)
    medium = models.URLField(max_length=255, default='', blank=True)
    wiki = models.URLField(max_length=255, default='', blank=True)
    twitter = models.URLField(max_length=255, default='', blank=True)
    facebook = models.URLField(max_length=255, default='', blank=True)
    telegram = models.URLField(max_length=255, default='', blank=True)
    youtube = models.URLField("Youtube", max_length=255, default='', blank=True)
    instagram = models.URLField("Instagram", max_length=255, default='', blank=True)
    linkedin = models.URLField("LinkedIn", max_length=255, default='', blank=True)
    bitcointalk = models.URLField("BitcoinTalk", max_length=255, default='', blank=True)
    google_plus = models.URLField("Google+", max_length=255, default='', blank=True)
    kakao = models.URLField("Kakao", max_length=255, default='', blank=True)
