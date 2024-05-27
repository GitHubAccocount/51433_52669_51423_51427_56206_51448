from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account import views

urlpatterns = [
  path('api/', include('account.urls')),
  path('api/books/', include('book.urls')),
  path('api/', include('borrowing.urls')),
  path('admin/', admin.site.urls),
  path('api/change-password/', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
