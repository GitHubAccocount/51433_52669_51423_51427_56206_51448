from django.urls import path
from . import views
from .views import book_detail_or_list 

urlpatterns = [
  path('', book_detail_or_list, name='book_list'),
  path('<str:pk>/', book_detail_or_list, name='book_detail'),
]