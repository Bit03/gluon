from haystack import indexes
from github.models import Repository, Organization


class OrganizationIndex(indexes.Indexable, indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=False)
    name = indexes.CharField(model_attr='name')
    bio = indexes.CharField(model_attr='bio')
    location = indexes.CharField(model_attr='location')
    web_site = indexes.CharField(model_attr='web_site')
    avatar = indexes.CharField(model_attr='avatar')
    star = indexes.IntegerField(default=0)
    # fork = indexes.IntegerField(default=0)
    # watch = indexes.IntegerField(default=0)

    def get_model(self):
        return Organization

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_star(self, obj):
        _star = 0
        repos = Repository.objects.filter(author=obj.author)
        for row in repos:
            _star += row.star
        return _star


class ReposIndex(indexes.Indexable, indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    name = indexes.CharField(model_attr='name')
    desc = indexes.CharField(model_attr='desc')

    created_at = indexes.DateTimeField(model_attr='created_at')
    updated_at = indexes.DateTimeField(model_attr='updated_at')

    star = indexes.IntegerField(model_attr='star', default=0, stored=True)
    watch = indexes.IntegerField(model_attr='watch', default=0, stored=True)
    fork = indexes.IntegerField(model_attr='fork', default=0, stored=True)

    latest_7_day_star = indexes.IntegerField(default=0, stored=True)
    latest_7_day_fork = indexes.IntegerField(default=0, stored=True)
    latest_7_day_watch = indexes.IntegerField(default=0, stored=True)

    def get_model(self):
        return Repository

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_latest_7_day_star(self, obj):
        star_sum = obj.stats_df(8).star.diff().fillna(0).sum()
        # print(star_sum)
        return int(star_sum)

    def prepare_latest_7_day_fork(self, obj):
        fork_sum = obj.stats_df(8).fork.diff().fillna(0).sum()
        return int(fork_sum)

    def prepare_latest_7_day_watch(self, obj):
        watch_sum = obj.stats_df(8).watch.diff().fillna(0).sum()
        return int(watch_sum)
