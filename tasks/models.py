from django.db import models

# Create your models here.

from django.db import models

class Task(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    startdate = models.DateTimeField()
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
