from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
  path('user_data', views.user_data, name='user_data'),
  path('register', views.register, name='register'),
  path('login', TokenObtainPairView.as_view(), name='token_obtain'),
  path('refresh', TokenRefreshView.as_view(), name='tokenrefresh'),
  path("user-list", views.user_list, name="user_list"),
]