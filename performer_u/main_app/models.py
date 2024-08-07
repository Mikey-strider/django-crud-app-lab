from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Instructor(models.Model):
    instructor_name = models.CharField(max_length=100)
    instruction_type = models.CharField(max_length=500)
    instructor_hours = models.DateTimeField('Date & Time')

    def __str__(self):
      return self.instructor_name

    def get_absolute_url(self):
      return reverse('instructor-detail', kwargs={'pk': self.id})


class Performer(models.Model):
    performer_name = models.CharField(max_length=100)
    performerance_type = models.CharField(max_length=150)
    performer_description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instructor = models.ManyToManyField(Instructor)

    def __str__(self):
      return self.performer_name

    def get_absolute_url(self):
      return reverse('perform-detail', kwargs={'perform_id': self.id})