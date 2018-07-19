from rest_framework import serializers


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

    watch = serializers.IntegerField(default=0, read_only=True)
    star = serializers.IntegerField(default=0, read_only=True)
    fork = serializers.IntegerField(default=0, read_only=True)

    latest_7_day_commit = serializers.IntegerField(default=0)
    latest_30_day_commit = serializers.IntegerField(default=0)
    latest_90_day_commit = serializers.IntegerField(default=0)

    ranking_latest_7_day = serializers.IntegerField(default=0)
    ranking_latest_30_day = serializers.IntegerField(default=0)
    ranking_latest_90_day = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass