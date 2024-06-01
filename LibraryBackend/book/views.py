from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.generics import get_object_or_404

from.models import Book
from.serializers import BookSerializer

@api_view(['GET'])
def book_detail_or_list(request, pk=None):  # Add pk parameter
    if pk:
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, context={'request': request})
    else:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
    return Response(serializer.data)