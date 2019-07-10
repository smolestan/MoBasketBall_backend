from rest_framework import routers
from .api import TrainingViewSet

router = routers.DefaultRouter()
router.register('training', TrainingViewSet, 'training')

urlpatterns = router.urls