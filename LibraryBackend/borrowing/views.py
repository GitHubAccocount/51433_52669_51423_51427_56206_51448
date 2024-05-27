from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound
from .models import Borrowing, Book
from .serializers import BorrowingSerializer

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    http_method_names = ['post', 'delete']

    def perform_create(self, serializer):
        borrowing = serializer.save()
        # Decrement book availability
        book = borrowing.book
        book.available -= 1
        book.save()
    def perform_destroy(self, instance):  # Returning a book
            borrowing = instance  # The borrowing record to be deleted
            book = borrowing.book
            if book:
                book.available += 1  # Increment available count
                book.save()
                borrowing.delete()  # Remove the borrowing record
            else:
                raise NotFound("Book not found")
