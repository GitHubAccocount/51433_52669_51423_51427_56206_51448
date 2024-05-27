from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BorrowingViewSet

router = DefaultRouter()
router.register(r'borrowings', BorrowingViewSet, basename='borrowing')

urlpatterns = [
    path('', include(router.urls)),
]
