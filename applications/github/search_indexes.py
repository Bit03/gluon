# import datetime
from datetime import datetime, timedelta
from haystack import indexes
from haystack.query import SearchQuerySet
from applications.github.models import (
    Repository,
    People,
)


# class OrganizationIndex(indexes.Indexable, indexes.SearchIndex):
#     text = indexes.CharField(document=True, use_template=False)
#     name = indexes.CharField(model_attr='name')
#     author = indexes.CharField(model_attr='author')
#     bio = indexes.CharField(model_attr='bio', null=True)
#     location = indexes.CharField(model_attr='location', null=True)
#     web_site = indexes.CharField(model_attr='web_site', null=True)
#     avatar = indexes.CharField(model_attr='avatar', null=True)
#     star = indexes.IntegerField(default=0)
#     fork = indexes.IntegerField(default=0)
#     watch = indexes.IntegerField(default=0)
#
#     def get_model(self):
#         return Organization
#
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()
#
#     def prepare_star(self, obj):
#         _star = 0
#         repos = SearchQuerySet().models(Repository).filter(author=obj.author)
#         for row in repos:
#             _star += row.star
#         return _star
#
#     def prepare_fork(self, obj):
#         _fork = 0
#         repos = SearchQuerySet().models(Repository).filter(author=obj.author)
#         for row in repos:
#             _fork += row.fork
#         return _fork
#
#     def prepare_watch(self, obj):
#         _watch = 0
#         repos = SearchQuerySet().models(Repository).filter(author=obj.author)
#         for row in repos:
#             _watch += row.watch
#         return _watch


class PeopleIndex(indexes.Indexable, indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name', null=True)
    login = indexes.CharField(model_attr='login')
    company = indexes.CharField(model_attr='company', null=True)
    bio = indexes.CharField(model_attr='bio', null=True)
    location = indexes.CharField(model_attr='location', null=True)
    email = indexes.CharField(model_attr='email', null=True)

    html_url = indexes.CharField(model_attr='html_url')

    def get_model(self):
        return People

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class ReposIndex(indexes.Indexable, indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    name = indexes.CharField(model_attr='name')
    desc = indexes.CharField(model_attr='desc', default='')

    created_at = indexes.DateTimeField(model_attr='created_at')
    updated_at = indexes.DateTimeField(model_attr='updated_at')

    star = indexes.IntegerField(model_attr='star', default=0, stored=True)
    watch = indexes.IntegerField(model_attr='watch', default=0, stored=True)
    fork = indexes.IntegerField(model_attr='fork', default=0, stored=True)

    latest_7_day_star = indexes.IntegerField(default=0, stored=True)
    latest_7_day_fork = indexes.IntegerField(default=0, stored=True)
    latest_7_day_watch = indexes.IntegerField(default=0, stored=True)

    latest_7_day_commit = indexes.IntegerField(default=0, stored=True)
    latest_30_day_commit = indexes.IntegerField(default=0, stored=True)
    latest_90_day_commit = indexes.IntegerField(default=0, stored=True)

    def get_model(self):
        return Repository

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_latest_7_day_star(self, obj):
        star_sum = obj.stats_df(8).sort_index().star.diff().fillna(0).sum()
        return int(star_sum)

    def prepare_latest_7_day_fork(self, obj):
        fork_sum = obj.stats_df(8).sort_index().fork.diff().fillna(0).sum()
        return int(fork_sum)

    def prepare_latest_7_day_watch(self, obj):
        watch_sum = obj.stats_df(8).sort_index().watch.diff().fillna(0).sum()
        return int(watch_sum)

    def prepare_latest_7_day_commit(self, obj):
        _start = datetime.now() - timedelta(days=7)
        _count = obj.commit.filter(commit_datetime__range=(_start, datetime.now())).count()
        return _count

    def prepare_latest_30_day_commit(self, obj):
        _start = datetime.now() - timedelta(days=30)
        _count = obj.commit.filter(commit_datetime__range=(_start, datetime.now())).count()
        return _count

    def prepare_latest_90_day_commit(self, obj):
        _start = datetime.now() - timedelta(days=90)
        _count = obj.commit.filter(commit_datetime__range=(_start, datetime.now())).count()
        return _count
