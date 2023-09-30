from django_filters import rest_framework as filters
from .models import Task


class TaskFilter(filters.FilterSet):
    time = filters.CharFilter(lookup_expr='gte', field_name='created_at')

    class Meta:
        model = Task
        fields = ('created_at',)
