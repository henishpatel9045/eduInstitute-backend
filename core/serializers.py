from rest_framework import serializers
from . import models

class CourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cources
        fields = '__all__'
        