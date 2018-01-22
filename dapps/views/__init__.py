from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from dapps.models import DApp


class DAppsListView(generic.ListView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/list.html'
    # template_name = 'web/index.html'
    paginate_by = 100

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


# class DappsFakeDetailView(generic.TemplateView):
#     template_name = 'web/detail.html'


class DAppsDetailView(LoginRequiredMixin,
                      generic.DetailView):
    model = DApp
    queryset = DApp.objects.all()
    template_name = 'dapps/detail.html'
    slug_field = 'slug'
