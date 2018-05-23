from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='DAppRank API')


urlpatterns = [
    # url(r'^token-auth/?$', views.obtain_auth_token),
    url(r'^auth/', include('rest_auth.urls')),
]

urlpatterns += [
    url(r'^dapps/', include('dapps.urls.api', namespace='dapps')),
    url(r'^github/', include('github.urls.api', namespace='github')),
]

urlpatterns += [
    url(r'^schema/$', schema_view, name='schema'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
