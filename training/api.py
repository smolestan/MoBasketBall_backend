from .models import Training, Exercise, Program, Course
from rest_framework import viewsets, permissions
from .serializers import TrainingSerializer, ExerciseSerializer, CourseSerializer, ProgramSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TrainingSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ExerciseSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProgramSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CourseSerializer