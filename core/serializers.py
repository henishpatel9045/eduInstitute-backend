from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class CourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cources
        fields = '__all__'
        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
