from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import (
    verify_jwt_token,
    refresh_jwt_token
)
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^docs/?$', get_swagger_view(title='DAppRank API'), name='docs'),
]

urlpatterns += [
    url(r'^dapps/', include('applications.dapps.urls.api', namespace='dapps')),
    url(r'^github/', include('applications.github.urls.api', namespace='github')),

    # auth api
    url(r'^auth/verify/?$', verify_jwt_token, name='verify'),
    url(r'^auth/refresh/?$', refresh_jwt_token, name='refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
