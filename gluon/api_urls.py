from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.urls import u


urlpatterns = [
    url(r'^token-auth/?$', obtain_jwt_token),
]

urlpatterns += [
    url(r'^dapps/', include('dapps.urls.api', namespace='dapp')),
    url(r'^github/', include('github.urls.api', namespace='github')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
