from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from . import models, serializers
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.
class CourceViewSet(ModelViewSet):
    queryset = models.Cources.objects.all()
    serializer_class = serializers.CourceSerializer
    
class StudentViewSet(ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    
    def list(self, request, *args, **kwargs):
        try:
            if self.request.user.is_staff:
                return super().list(request, *args, **kwargs)
            else:
                return Response("You are not authorised to view Student Data.", status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response("Use valid access tocken.", status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):    
        try:
            if self.request.user.is_staff:
                return super().retrieve(request, *args, **kwargs)
            else:
                return Response("You are not authorised to view Student Data.", status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response("Use valid access tocken.", status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False)
    def me(self, request):
        try:
            student = models.Student.objects.get(user__id=request.user.id)
            if student:
                student = serializers.StudentSerializer(student)    
                return Response(student.data, status=status.HTTP_200_OK)   
            else:
                return Response("Please logIn using valid access tocken.", status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response("Add access token in request header. i.e. KEY=Authorization VALUE= JWT your_access_tocken", status=status.HTTP_400_BAD_REQUEST)
    