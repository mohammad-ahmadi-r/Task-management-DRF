import datetime

from rest_framework import serializers
from .models import Task


class TaskSerializers(serializers.HyperlinkedModelSerializer):
    go_to_task = serializers.HyperlinkedIdentityField(
        view_name='api:task-detail', lookup_field='pk', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['url', 'title', 'description', 'go_to_task']
        # read_only_fields = (
        #     'url',
        #     'title',
        #     'description',
        #     'go_to_task',
        # )
        # fields = read_only_fields + ('completed',)


class TaskSerializersDetails(serializers.ModelSerializer):
    batman = serializers.IntegerField(default=5, read_only=True)
    superman = serializers.CharField(default='ya alllah', read_only=True)
    titlee = serializers.DateTimeField(default=datetime.datetime.now(), read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


