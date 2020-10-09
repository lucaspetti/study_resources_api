from django.test import TestCase
from .models import Subject
from .models import Resource

class SubjectTestCase(TestCase):
  def setUp(self):
    Subject.objects.create(name='Databases')

  def test_subjects_name(self):
    databases = Subject.objects.get(name='Databases')
    self.assertEqual(databases.__str__(), 'Databases')

class ResourceTestCase(TestCase):
  def setUp(self):
    Subject.objects.create(name='Databases')
    subject = Subject.objects.get(name='Databases')
    Resource.objects.create(name='CS_DB_CLASS', subject=subject)

  def test_resources_name(self):
    resource = Resource.objects.get(name='CS_DB_CLASS')
    self.assertEqual(resource.__str__(), 'CS_DB_CLASS')
