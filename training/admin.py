from django.contrib import admin
from .models import Training, Course, Program, Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_filter = ['training']

class TrainingAdmin(admin.ModelAdmin):
    list_filter = ['program']

class ProgramAdmin(admin.ModelAdmin):
    list_filter = ['course']


# Register your models here.
admin.site.register(Training, TrainingAdmin)
admin.site.register(Course)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Exercise, ExerciseAdmin)