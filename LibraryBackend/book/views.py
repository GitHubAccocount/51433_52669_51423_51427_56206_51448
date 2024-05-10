from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request

from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request: Request):
  books = Book.objects.all()

  serializer = BookSerializer(books, many=True, context={'request': request})

  return JsonResponse({'books': serializer.data})
