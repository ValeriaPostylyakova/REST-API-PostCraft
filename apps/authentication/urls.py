from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, CustomTokenRefreshView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path


router = DefaultRouter()

router.register('auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('auth/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += router.urls