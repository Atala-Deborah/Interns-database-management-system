from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class Intern(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Workshop(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='workshop_images/')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_finished = models.BooleanField(default=False)
    
    def is_past(self):
        return timezone.now().date() > self.date

    def __str__(self):
        return self.title

from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('not_started', 'Not Started'),
    ]

    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    project = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.project}"
