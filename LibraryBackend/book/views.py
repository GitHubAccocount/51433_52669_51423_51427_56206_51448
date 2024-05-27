from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from.models import Book
from.serializers import BookSerializer

@api_view(['GET']) 
def book_list(request: Request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True, context={'request': request})
    return Response({'books': serializer.data})