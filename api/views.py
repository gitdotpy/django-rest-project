from rest_framework import mixins, viewsets
from rest_framework import permissions
from .serializers import SchoolsSerializer
from .filters import SchoolsFilter
from school.models import Schools

# Create your views here.

class SchoolsView(
  mixins.CreateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  viewsets.GenericViewSet,
):

  queryset = Schools.objects.all()
  serializer_class = SchoolsSerializer
  filterset_class = SchoolsFilter
  #permission_classes = [permissions.IsAuthenticated]
