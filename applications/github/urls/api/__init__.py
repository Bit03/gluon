from django.conf.urls import url, include

# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # url(r'^org/', include('applications.github.urls.api.org', namespace='org')),
    url(r'^users/', include('applications.github.urls.api.people', namespace='people')),
    url(r'^repos/', include('applications.github.urls.api.repos', namespace='repos')),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

