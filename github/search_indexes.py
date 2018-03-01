from haystack import indexes
from github.models import Repository


class ReposIndex(indexes.Indexable, indexes.SearchIndex):

    def get_model(self):
        return Repository


# from articles.models import Article


# class ArticleIndex(indexes.Indexable, indexes.SearchIndex):
#     text = indexes.CharField(document=True, use_template=True)
#     author = indexes.FacetIntegerField(model_attr="author_id")
#     category = indexes.FacetIntegerField(model_attr="category_id")
#     title = indexes.CharField(model_attr="title", boost=10)
#     digest = indexes.CharField(model_attr="digest", boost=5)
#     absolute_url = indexes.CharField(model_attr="get_absolute_url")
#     status = indexes.CharField(model_attr="status")
#     highlight = indexes.BooleanField(model_attr="highlight")
#
#     tags = indexes.FacetMultiValueField()
#     keywords = indexes.FacetMultiValueField()
#
#     created_at = indexes.DateTimeField(model_attr='created_at')
#     updated_at = indexes.DateTimeField(model_attr='updated_at')
#     published_at = indexes.DateTimeField(model_attr='published_at')
#
#     cover_url = indexes.CharField(model_attr='cover_url')
#     author_name = indexes.CharField(model_attr='author_name', default="")
#     author_url = indexes.CharField(model_attr='author_url')
#     author_avatar_url = indexes.CharField(model_attr='author_avatar_url')
#     # author_
#
#     def get_model(self):
#         return Article
#
#     def index_queryset(self, using=None):
#         return self.get_model().objects.filter(author__isnull=False)
#
#     def get_updated_field(self):
#         return 'updated_at'
#
#     def prepare_tags(self, obj):
#         return [o.name for o in obj.tags.all()]
#
#     def prepare_keywords(self, obj):
#         return obj.keywords
