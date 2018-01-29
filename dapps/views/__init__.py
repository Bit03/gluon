from django.views import generic
from django_filters import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from dapps.models import DApp


class DAppSearchListView(LoginRequiredMixin,
                         generic.ListView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/list.html'
    paginate_by = 100

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(Q(name__icontains=self.query))

    def get(self, request, *args, **kwargs):
        self.query = request.GET.get('q', None)
        return super().get(request, *args, **kwargs)


class DAppsListView(LoginRequiredMixin,
                    views.FilterView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/list.html'
    # template_name = 'web/index.html'
    paginate_by = 100
    filter_fields = ("status", "ico_status", "platform")

    def get_context_data(self, **kwargs):
        '''
        加入30个假的项目
        稍后替换
        :param kwargs:
        :return:
        '''
        context = super().get_context_data(**kwargs)
        context['rg'] = range(30)
        return context


class DAppsDetailView(LoginRequiredMixin,
                      generic.DetailView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/detail.html'
    slug_field = 'slug'
