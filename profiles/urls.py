from rest_framework import routers
from .api import ProfileViewSet

router = routers.DefaultRouter()
router.register('', ProfileViewSet, 'profile')
router.register('<pk>', ProfileViewSet, 'update')

urlpatterns = router.urls