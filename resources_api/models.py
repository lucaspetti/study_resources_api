from django.db import models

class Subject(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Resource(models.Model):
  name = models.CharField(max_length=100)
  kind = models.CharField(null=True, max_length=50)
  description = models.TextField(null=True)
  link = models.CharField(null=True, max_length=300)
  status = models.CharField(
    max_length=20,
    choices=['to_do', 'in_progress', 'done', 'review'],
  )
  subject = models.ForeignKey(Subject, related_name='resources', on_delete=models.CASCADE, null=True)

  def __str__(self):
      return self.name
