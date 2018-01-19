from django.conf.urls import url
from dapps.views import DAppsListView


urlpatterns = [
    url(r'^$', DAppsListView.as_view(), name='list'),
]