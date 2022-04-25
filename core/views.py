from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from django.contrib.auth.models import User

# Create your views here.
class CourceViewSet(ModelViewSet):
    queryset = models.Cources.objects.all()
    serializer_class = serializers.CourceSerializer
    
class StudentViewSet(ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    
    