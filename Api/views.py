from django.shortcuts import render
from .models import studentmodel
from .serializers import Studentsrializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class modelviewsets(viewsets.ModelViewSet):
    queryset=studentmodel.objects.all()
    serializer_class=Studentsrializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]



