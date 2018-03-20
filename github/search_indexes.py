from haystack import indexes
from github.models import Repository


class ReposIndex(indexes.Indexable, indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    name = indexes.CharField(model_attr='name')
    desc = indexes.CharField(model_attr='desc')

    created_at = indexes.DateTimeField(model_attr='created_at')
    updated_at = indexes.DateTimeField(model_attr='updated_at')

    star = indexes.IntegerField(model_attr='star')
    watch = indexes.IntegerField(model_attr='watch')
    fork = indexes.IntegerField(model_attr='fork')

    def get_model(self):
        return Repository

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
