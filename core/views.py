from rest_framework.viewsets import ModelViewSet
from . import models, serializers

# Create your views here.
class CourceViewSet(ModelViewSet):
    queryset = models.Cources.objects.all()
    serializer_class = serializers.CourceSerializer
    