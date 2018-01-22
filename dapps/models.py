# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import urlresolvers
from django.db import models
from model_utils.models import SoftDeletableModel
from model_utils.fields import StatusField
from model_utils import Choices
from django_extensions.db import fields

# Create your models here.
from django.utils import timezone
from taggit.managers import TaggableManager


class DApp(SoftDeletableModel):
    # Platform = Choices("")
    ICO_STATUS_CHOICES = Choices("Planned", "Active", "Complate")
    STATUS = Choices("demo", "live", "concept", "wip")
    LICENSE_CHOICES = Choices("MIT", "GPLv3", "Apache License 2.0", "proprietary", "GPL")

    slug = fields.RandomCharField(length=12, unique=True,
                                  include_alpha=False, db_index=True, editable=False)
    name = models.CharField(max_length=64, )
    platform = models.CharField(max_length=64, )
    symbol = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(blank=True, default='')
    description_cn = models.TextField(blank=True, default='')
    country_of_origin = models.CharField(max_length=64, default='')

    faq = models.CharField(max_length=255, default='')
    founder = models.CharField(max_length=255, default='')
    vc = models.CharField(max_length=255, default='')
    etherian = models.CharField(max_length=255, default='')

    license = StatusField(choices_name='LICENSE_CHOICES')
    status = StatusField(choices_name='STATUS')
    ico_status = StatusField(choices_name='ICO_STATUS_CHOICES')

    submitted = models.DateTimeField(null=True, blank=True, db_index=True)
    last_update = models.DateTimeField(null=True, blank=True, db_index=True)

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    tags = TaggableManager()

    class Meta:
        verbose_name = "Decentralised Applications"
        verbose_name_plural = "Decentralised Applications"
        ordering = ("last_update", )

    def __str__(self):
        return self.name

    @property
    def tag_list(self):
        return u", ".join(o.name for o in self.tags.all())

    def get_absolute_url(self):
        return urlresolvers.reverse('dapps:detail', args=[self.slug, ])


class ContractAddress(models.Model):
    dapp = models.OneToOneField(DApp, related_name='contract')
    mainnet = models.CharField(max_length=128, null=True)
    ropsten = models.CharField(max_length=128, null=True)
    kovan = models.CharField(max_length=128, null=True)
    rinkeby = models.CharField(max_length=128, null=True)

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
    whitepaper = models.URLField(max_length=1024)

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Site"

    def __str__(self):
        return self.url


class GitHub(models.Model):
    dapp = models.OneToOneField(DApp, related_name='github')
    url = models.URLField(max_length=255)
    readme = models.TextField()

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    def __str__(self):
        return self.url


class Social(models.Model):
    dapp = models.OneToOneField(DApp, related_name='social')
    reddit = models.URLField(max_length=255, default='')
    slack = models.URLField(max_length=255, default='')
    gitter = models.URLField(max_length=255, default='')
    blog = models.URLField(max_length=255, default='')
    medium = models.URLField(max_length=255, default='')
    wiki = models.URLField(max_length=255, default='')
    twitter = models.URLField(max_length=255, default='')
    facebook = models.URLField(max_length=255, default='')
    telegram = models.URLField(max_length=255, default='')
    youtube = models.URLField("Youtube", max_length=255, default='')
    instagram = models.URLField("Instagram", max_length=255, default='')
    linkedin = models.URLField("LinkedIn", max_length=255, default='')
    bitcointalk = models.URLField("BitcoinTalk", max_length=255, default='')
    google_plus = models.URLField("Google+", max_length=255, default='')
    kakao = models.URLField("Kakao", max_length=255, default='')
