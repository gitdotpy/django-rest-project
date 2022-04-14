from rest_framework.serializers import ModelSerializer
from school.models import Schools

class SchoolsSerializer(ModelSerializer):
  class Meta:
    model = Schools
    fields = ('__all__')