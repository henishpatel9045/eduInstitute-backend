from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class CourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cources
        fields = '__all__'
        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
    