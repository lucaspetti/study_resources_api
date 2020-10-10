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
  subject = models.ForeignKey(
    Subject,
    related_name='resources',
    on_delete=models.CASCADE,
    null=True
  )
  STATUS_CHOICES = (
    ('TO_DO', 'to_do'),
    ('WIP', 'in_progress'),
    ('DONE', 'done'),
    ('REV', 'review'),
  )
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='TO_DO',
  )


  def __str__(self):
      return self.name
