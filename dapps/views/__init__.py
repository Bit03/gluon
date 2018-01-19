from django.views import generic
from dapps.models import DApp


class DAppsListView(generic.ListView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/list.html'
