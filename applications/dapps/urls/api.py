from django.conf.urls import url
from applications.dapps.views.api import DAppListAPIView


urlpatterns = [
    url(r'^$', DAppListAPIView.as_view(), name='list'),
]

