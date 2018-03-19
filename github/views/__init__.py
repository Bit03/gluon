import logging
from django.views import generic
from github.models import Organization, People, Repository

logger = logging.getLogger('django')


class GitHubListView(generic.ListView):
    model = Organization
    template_name = 'github/list.html'
    paginate_by = 60


class ReposListView(generic.ListView):
    model = Repository
    template_name = 'github/repos/list.html'
    paginate_by = 30

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.author)
        logger.info(qs)
        return qs

    def get(self, request, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        return super().get(request, *args, **kwargs)
