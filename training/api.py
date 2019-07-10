from .models import Training
from rest_framework import viewsets, permissions
from .serializers import TrainingSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TrainingSerializer