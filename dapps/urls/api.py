from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dapps.views.api import DAppListAPIView


urlpatterns = [
    url(r'^$', DAppListAPIView.as_view(), name='list'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

