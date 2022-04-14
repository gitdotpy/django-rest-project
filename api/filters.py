import django_filters
from school.models import Schools

class SchoolsFilter(django_filters.FilterSet):

  class Meta:
    model = Schools
    fields = ('__all__')