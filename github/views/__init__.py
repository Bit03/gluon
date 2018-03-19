import logging
from django.views import generic
from github.models import Organization, People, Repository

import pygal
from pygal.style import DarkSolarizedStyle

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


class ReposDetailView(generic.DetailView):
    model = Repository
    template_name = 'github/repos/detail.html'
    queryset = Repository.objects.all()
    slug_field = 'identified_code'

    def get_context_data(self, **kwargs):
        # _context = super(ProjectDetailView, self).get_context_data(**kwargs)

        # _status = Status.objects.filter(project=self.object,
        #                                 datetime__gte=datetime.now() - timedelta(31)
        #                                 ).order_by('datetime')
        # chart = self.get_chart(_status)
        #
        # _context.update({
        #     'meta': {
        #         'author': self.object.author,
        #     },
        #     'chart': chart.render_data_uri(show_dots=True),
        # })
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
