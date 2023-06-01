from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='course_images', blank=True, null=True)

    def __str__(self):
        return self.name

    def is_current(self):
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date

    @classmethod
    def planned_courses(cls):
        today = timezone.now().date()
        return cls.objects.filter(start_date__gte=today)
