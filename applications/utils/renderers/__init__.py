import json

from rest_framework.renderers import BaseRenderer


class ChartRenderer(BaseRenderer):
    media_type = 'application/json'
    format = 'chart'
    charset = 'utf-8'
    render_style = 'text'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        ret = list(map(lambda x: [x['timestamp'], x['commit_count']], data))
        return json.dumps(ret)
