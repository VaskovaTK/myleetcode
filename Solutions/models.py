from django.db import models
from Problems.models import Task

class Solved (models.Model):
    objects = models.Manager()
    title = Task.title
    solution = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

