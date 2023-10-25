from .models import studentmodel
from rest_framework import serializers

class Studentsrializer(serializers.ModelSerializer):
    class Meta:
        model=studentmodel
        fields=['id','name','age','roll']
        
