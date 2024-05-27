from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render
from django.http import JsonResponse
from.serializer import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def user_data(request):
    return JsonResponse({
        'id': request.user.id,
        'email': request.user.email
    })

@api_view(['POST'])  # Define this function as a view that only accepts POST requests
@authentication_classes([])  # No authentication required for this view
@permission_classes([])  # No specific permissions required for this view

def register(request):
    """
    Register a new user.

    Expects a JSON object containing user information including email and password.
    Validates the data using a serializer, saves the user to the database if the data is valid,
    and returns a success response with HTTP status code 201.

    If the data is invalid, returns a JSON response with details about the validation errors
    and HTTP status code 400.

    Args:
        request: HTTP request object containing user data in JSON format

    Returns:
        JSON response containing either a success message or validation errors
    """
    serializer = UserSerializer(data=request.data)  # Initialize the serializer with request data
    if serializer.is_valid():  # Check if the data passes validation
        serializer.save()  # Save the user to the database
        return JsonResponse({'status': 'success'}, status=201)  # Return success response
    else:  # If data is invalid
        return JsonResponse(serializer.errors, status=400)  # Return validation errors as JSON response

@api_view(['PATCH'])  # Define this function as a view that only accepts PATCH requests
@authentication_classes([])  # No authentication required for this view (assuming you'll add auth later)
@permission_classes([])  # No specific permissions required for this view (assuming you'll add perms later)

def change_password(request):
    """
    Change the password for the current user.

    Expects a JSON object containing the old password and the new password.
    Validates the old password, updates the user's password if valid,
    and returns a success response with HTTP status code 200.

    If the old password is invalid, returns a JSON response with an error message
    and HTTP status code 400.

    Args:
        request: HTTP request object containing old and new password in JSON format

    Returns:
        JSON response containing either a success message or an error message
    """
    user = request.user  # Get the current user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    if not user.check_password(old_password):
        return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

    user.password = make_password(new_password)  # Hash and set the new password
    user.save()

    return Response({'status': 'Password changed successfully'}, status=status.HTTP_200_OK)