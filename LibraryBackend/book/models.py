from django.db import models
import uuid

class Book(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=255, blank=False)
  author = models.CharField(max_length=100, blank=False)
  image = models.ImageField(upload_to='files/covers', blank=True, null=True)
  year_published = models.PositiveIntegerField(blank=True, null=True)
  category = models.CharField(max_length=100, blank=True)
  description = models.TextField(blank=True)
