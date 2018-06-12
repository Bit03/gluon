from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    # url(r'^token-auth/?$', views.obtain_auth_token),
    # url(r'^auth/', include('rest_auth.urls')),
    url(r'^docs/?$', get_swagger_view(title='DAppRank API'), name='docs'),
]

urlpatterns += [
    url(r'^dapps/', include('dapps.urls.api', namespace='dapps')),
    url(r'^github/', include('github.urls.api', namespace='github')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
