from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from.models import Book, Loan
from.serializers import BookSerializer, LoanSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def book_list(request: Request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response({'books': serializer.data})
    elif request.method == 'POST':
        data = request.data
        if 'book_id' not in data:
            return Response({'error': 'Book ID is required'}, status=400)
        try:
            book_id = data['book_id']
            book = Book.objects.get(id=book_id)
            loan = Loan(book=book, borrower=request.user)
            loan.reserve()
            serializer = LoanSerializer(loan, context={'request': request})
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def loan_list(request: Request):
    loans = Loan.objects.all()
    serializer = LoanSerializer(loans, many=True, context={'request': request})
    return Response({'loans': serializer.data})