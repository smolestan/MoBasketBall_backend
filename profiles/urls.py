from rest_framework import routers
from .api import ProfileViewSet

router = routers.DefaultRouter()
router.register('', ProfileViewSet, 'profile')

urlpatterns = router.urls