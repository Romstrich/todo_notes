from django_filters import rest_framework as filters

from .models import Todo

class TodoFilter(filters.FilterSet):
    #project=filters.CharFilter(lookup_expr='contains')

    class Meta:
        model=Todo
        fields=['project']