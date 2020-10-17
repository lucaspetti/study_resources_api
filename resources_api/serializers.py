from rest_framework import serializers

from .models import Subject
from .models import Resource

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Subject
    fields = '__all__'

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Resource
    fields = ('id', 'name', 'kind', 'description', 'link', 'status', 'subject')
