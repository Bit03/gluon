from django.conf.urls import url
from github.views.api import RepositoryListAPIView

urlpatterns = [
    url(r'^$', RepositoryListAPIView.as_view(), name='list'),
]
