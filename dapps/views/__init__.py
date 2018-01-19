from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from dapps.models import DApp


class DAppsListView(
                    generic.ListView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/list.html'
