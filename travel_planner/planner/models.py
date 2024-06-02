# planner/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    assigned_to = models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    skills = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
