from rest_framework.routers import DefaultRouter
from .views import AuthViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path


router = DefaultRouter()

router.register('auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('auth/refresh/', TokenRefreshView.as_view()),

]

urlpatterns += router.urls