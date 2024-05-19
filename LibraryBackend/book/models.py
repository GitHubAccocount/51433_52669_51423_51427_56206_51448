from django.db import models
import uuid

import os

def default_image_path():
    return 'covers/defaultCover.png'  # Path to the default photo

class Book(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=255, blank=False)
  author = models.CharField(max_length=100, blank=False)
  image = models.ImageField(upload_to='covers/', blank=True, null=True, default=default_image_path)
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

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=true) #Ensures email uniqueness
    # Temporary excluded from code - phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)  # Automatically set loan date
    return_date = models.DateField(null=True, blank=True)  # Allow null return dates for active loans
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('returned', 'Returned'), ('overdue', 'Overdue')], default='active')

    def __str__(self):
        return f'Loan of {self.book.title} to {self.borrower.name}'