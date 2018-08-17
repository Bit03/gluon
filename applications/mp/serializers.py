from rest_framework import serializers
from haystack.query import SearchQuerySet
from applications.github.models import People
from applications.dapps.models import DApp


class PeopleRankSerializer(serializers.Serializer):
    name = serializers.CharField()
    login = serializers.CharField()
    avatar = serializers.URLField()

    watch = serializers.IntegerField(default=0, read_only=True)
    star = serializers.IntegerField(default=0, read_only=True)
    fork = serializers.IntegerField(default=0, read_only=True)

    latest_7_day_commit = serializers.IntegerField(default=0)
    latest_30_day_commit = serializers.IntegerField(default=0)
    latest_90_day_commit = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class PeopleRankDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    login = serializers.CharField()
    avatar = serializers.URLField()

    white_paper = serializers.SerializerMethodField(read_only=True)

    watch = serializers.IntegerField(default=0, read_only=True)
    star = serializers.IntegerField(default=0, read_only=True)
    fork = serializers.IntegerField(default=0, read_only=True)

    latest_7_day_commit = serializers.IntegerField(default=0)
    latest_30_day_commit = serializers.IntegerField(default=0)
    latest_90_day_commit = serializers.IntegerField(default=0)

    ranking_latest_7_day = serializers.SerializerMethodField(default=0)
    ranking_latest_30_day = serializers.SerializerMethodField(default=0)
    ranking_latest_90_day = serializers.SerializerMethodField(default=0)

    def get_ranking_latest_7_day(self, obj):
        sqs = SearchQuerySet().models(People).all().order_by('-latest_7_day_commit').values_list('pk', flat=True)
        index = list(sqs).index("{}".format(obj.pk)) + 1
        return index

    def get_ranking_latest_30_day(self, obj):
        sqs = SearchQuerySet().models(People).all().order_by('-latest_30_day_commit').values_list('pk', flat=True)
        index = list(sqs).index("{}".format(obj.pk)) + 1
        return index

    def get_ranking_latest_90_day(self, obj):
        sqs = SearchQuerySet().models(People).all().order_by('-latest_90_day_commit').values_list('pk', flat=True)
        index = list(sqs).index("{}".format(obj.pk)) + 1
        return index

    def get_white_paper(self, obj):
        try:
            _dapp = DApp.objects.get(github__login=obj.login)
            return _dapp.site.whitepaper
        except DApp.DoesNotExist:
            return ''

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
