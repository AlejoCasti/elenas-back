from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
  class Status(models.TextChoices):
    COMPLETED = 'completed'
    PENDING = 'pending'

  title = models.CharField(max_length=100, default='')
  description = models.CharField(max_length=500, default='')
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  status = models.CharField(
    max_length=10,
    choices=Status.choices,
    default=Status.PENDING,
  )
