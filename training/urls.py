from rest_framework import routers
from .api import TrainingViewSet, ExerciseViewSet, ProgramViewSet, CourseViewSet

router = routers.DefaultRouter()
router.register('trainings', TrainingViewSet, 'training')
router.register('exercises', ExerciseViewSet, 'exercise')
router.register('programs', ProgramViewSet, 'program')
router.register('courses', CourseViewSet, 'course')

urlpatterns = router.urls