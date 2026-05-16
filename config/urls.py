from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path(f'{settings.ADMIN_PANEL_PATH}/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
			 
	path('api/', include('apps.authentication.urls')),
    path('api/v1/', include('apps.profiles.urls')),
    path('api/v1/', include('apps.posts.urls')),
    path('api/v1/', include('apps.comments.urls')),
	path('api/v1/', include('apps.tags.urls')),
    path('api/v1/', include('apps.categories.urls')),
]
