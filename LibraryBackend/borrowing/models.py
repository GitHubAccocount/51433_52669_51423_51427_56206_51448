from django.db import models
import uuid
from account.models import User
from book.models import Book
from django.utils import timezone

class Borrowing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, to_field="id")
    borrowed_at = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.return_date = self.borrowed_at + timezone.timedelta(days=60)
        super().save(*args, **kwargs)
