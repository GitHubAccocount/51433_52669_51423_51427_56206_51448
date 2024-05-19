from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request

from.models import Book, Loan
from.serializers import BookSerializer, LoanSerializer

@api_view(['GET', 'POST'])
def book_list(request: Request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return JsonResponse({'books': serializer.data})
    elif request.method == 'POST':
        data = request.data
        book_id = data['book_id']
        book = Book.objects.get(id=book_id)
        loan = Loan(book=book, borrower=request.user)
        loan.reserve()
        serializer = LoanSerializer(loan, context={'request': request})
        return JsonResponse(serializer.data)

@api_view(['GET'])
def loan_list(request: Request):
    loans = Loan.objects.all()
    serializer = LoanSerializer(loans, many=True, context={'request': request})
    return JsonResponse({'loans': serializer.data})
