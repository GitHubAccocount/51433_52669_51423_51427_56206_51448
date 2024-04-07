from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import UserSerializer

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return JsonResponse({'status': 'success'}, status=201)
  return JsonResponse(serializer.errors, status=400)