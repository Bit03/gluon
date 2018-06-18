import logging

import pygal
from django.views import generic
from haystack.query import SearchQuerySet
from pygal.style import DarkSolarizedStyle

from applications.github.models import (
    Organization,
    Repository
)

logger = logging.getLogger('django')


class GitHubListView(generic.ListView):
    model = Organization
    template_name = 'github/list.html'
    paginate_by = 60

    def get_queryset(self):
        qs = SearchQuerySet().models(Organization).all().order_by('-star')
        return qs


class ReposListView(generic.ListView):
    model = Repository
    template_name = 'github/repos/list.html'
    paginate_by = 30
    queryset = Repository.objects.all()

    def get_queryset(self):
        qs = SearchQuerySet().filter(author=self.author).order_by("-latest_7_day_star")
        return qs

    def get(self, request, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        return super().get(request, *args, **kwargs)


class ReposDetailView(generic.DetailView):
    model = Repository
    template_name = 'github/repos/detail.html'
    queryset = Repository.objects.all()
    slug_field = 'identified_code'

    def get_context_data(self, **kwargs):
        _context = super().get_context_data()
        _chart = self.get_chart()

        _context.update({
            'chart': _chart.render_data_uri(show_dots=True),
        })

        return _context

    def get_chart(self):
        df = self.object.stats_df()
        line_chat = pygal.Line(x_label_rotation=90,
                               width=600, height=300,
                               pretty_print=True,
                               interpolate='cubic', style=DarkSolarizedStyle)
        line_chat.human_readable = True
        line_chat.x_labels =  map(lambda x: x.strftime("%Y-%m-%d"), df.index.tolist())
        star_se = df.star.diff().fillna(0)
        fork_se = df.fork.diff().fillna(0)
        watch_se = df.watch.diff().fillna(0)
        line_chat.add('star', star_se.tolist())
        line_chat.add('fork', fork_se.tolist())
        line_chat.add('watch', watch_se.tolist())
        line_chat.title = self.object.name
        return line_chat
