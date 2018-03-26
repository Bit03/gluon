"""gluon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import (LoginView, LogoutView)
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


urlpatterns += [
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^dapps/', include('dapps.urls', namespace='dapps')),
    url(r'^github/', include('github.urls', namespace='github')),
]

urlpatterns += [
    url(r'^login/$', LoginView.as_view(
        template_name="accounts/login.html",
    ), name='login'),
]


# API
urlpatterns += [
    url(r'^api/', include('gluon.urls.api', namespace="api")),

    url(r'^docs/', include_docs_urls(title='Baryon API Docs',
                                     public=False,
                                     permission_classes=[
                                         permissions.IsAdminUser,
                                     ])
        ),
]

urlpatterns += [
    url(r'^', include('cms.urls')),
]