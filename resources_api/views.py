from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import SubjectSerializer
from .serializers import ResourceSerializer

from .models import Subject
from .models import Resource

class SubjectViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  queryset = Subject.objects.all().order_by('name')
  serializer_class = SubjectSerializer

class ResourceViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  queryset = Resource.objects.all().order_by('name')
  serializer_class = ResourceSerializer
