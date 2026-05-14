from django.urls import path
from .views import (register, login, logout, get_current_user, get_users)
from rest_framework_simplejwt.views import (
	TokenRefreshView,
)

urlpatterns = [
   path('register/', register),
	 path('login/', login),
	 path('refresh/', TokenRefreshView.as_view()),
	 path('logout/', logout),
	 path('current-user/', get_current_user),
	 path('users/', get_users),
]