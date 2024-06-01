from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound
from .models import Borrowing, Book
from .serializers import BorrowingSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        # Ensure only superusers can create a borrowing
        self.check_object_permissions(self.request, serializer.instance)
        borrowing = serializer.save()
        # Decrement book availability
        book = borrowing.book
        book.available -= 1
        book.save()

    def perform_destroy(self, instance):
        # Ensure only superusers can delete a borrowing
        self.check_object_permissions(self.request, instance)
        borrowing = instance  # The borrowing record to be deleted
        book = borrowing.book
        if book:
            book.available += 1  # Increment available count
            book.save()
            borrowing.delete()  # Remove the borrowing record
        else:
            raise NotFound("Book not found")

    def retrieve(self, request, pk=None):
        borrowing = get_object_or_404(Borrowing, pk=pk, return_date__isnull=False)  # Use 'return_date'
        serializer = self.get_serializer(borrowing)
        return Response(serializer.data)

    def list(self, request):
        # Ensure only superusers can list borrowings
        self.check_permissions(self.request)
        borrowed_books = Borrowing.objects.all()
        serializer = self.get_serializer(borrowed_books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_borrowings(self, request):
        user = request.user
        borrowings = Borrowing.objects.filter(user=user)
        serializer = self.get_serializer(borrowings, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'list']:
            self.permission_classes = [IsSuperUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
