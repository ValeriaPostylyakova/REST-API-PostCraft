from .views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('profiles', ProfileViewSet, basename='profiles')

urlpatterns = router.urls