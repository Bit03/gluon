from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from views.index import IndexView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^github/', include('applications.github.urls', namespace='github')),

]

# API
urlpatterns += [
    url(r'^api/', include('gluon.urls.api', namespace="api")),
]

urlpatterns += [
    url(r'^.*$', IndexView.as_view(), name='index'),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
                          url(r'^__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
