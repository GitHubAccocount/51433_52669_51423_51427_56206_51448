from django.db import models
import uuid

import os

class Book(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=255, blank=False)
  author = models.CharField(max_length=100, blank=False)
  image = models.ImageField(upload_to='covers/', blank=True, null=True)
  year_published = models.PositiveIntegerField(blank=True, null=True)
  category = models.CharField(max_length=100, blank=True)
  description = models.TextField(blank=True)
  total_stock = models.PositiveIntegerField(default=0)
  available = models.PositiveIntegerField(default=0) 

  def save(self, *args, **kwargs):
    # Delete old image when a new one is uploaded
    try:
        old_instance = Book.objects.get(id=self.id)
        if old_instance.image and self.image and old_instance.image != self.image:
            if os.path.isfile(old_instance.image.path):
                os.remove(old_instance.image.path)
    except Book.DoesNotExist:
        pass

    super(Book, self).save(*args, **kwargs)