from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('api/', include('apps.authentication.urls')),
    path('api/v1/', include('apps.profiles.urls')),
    path('api/v1/', include('apps.posts.urls')),
    path('api/v1/', include('apps.comments.urls')),
	path('api/v1/', include('apps.tags.urls')),
    path('api/v1/', include('apps.categories.urls')),
]
