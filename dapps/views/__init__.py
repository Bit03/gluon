from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from dapps.models import DApp


class DAppsListView(LoginRequiredMixin,
                    generic.ListView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/list.html'
    paginate_by = 100


class DAppsDetailView(LoginRequiredMixin,
                      generic.DetailView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/detail.html'
    slug_field = 'slug'
