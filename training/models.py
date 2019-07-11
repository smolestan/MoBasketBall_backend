from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.title

class Training(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    program = models.ManyToManyField(Program)
    LEVEL_CHOICES = (
        ('beginner', 'beginner'),
        ('medium', 'medium'),
        ('pro', 'pro')
    )
    level = models.CharField(max_length=64, choices=LEVEL_CHOICES, default="medium")

    def __str__(self):
        return self.title

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    training = models.ManyToManyField(Training)
    video = models.FileField(upload_to='vids', blank=True, null=True)

    def __str__(self):
        return self.title

