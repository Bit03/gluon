from django.conf.urls import url
from applications.dapps.views.api import (
    DAppListAPIView,
    DAppPlatformAPIView,
    DAppDetailAPIView,
)


urlpatterns = [
    url(r'^$', DAppListAPIView.as_view(), name='list'),
    url(r'^platform/?$', DAppPlatformAPIView.as_view(), name='platform'),
    url(r'^(?P<slug>\d+)/?$', DAppDetailAPIView.as_view(), name='detail'),
]

