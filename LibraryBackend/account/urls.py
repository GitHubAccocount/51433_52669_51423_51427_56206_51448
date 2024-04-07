from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('/login', TokenObtainPairView.as_view(), name='token_obtain'),
  path('/refresh', TokenRefreshView.as_view(), name='tokenrefresh')
]