from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from github.views.api import AuthorListAPIView


urlpatterns = [
    url(r'^$', AuthorListAPIView.as_view(), name='list'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

