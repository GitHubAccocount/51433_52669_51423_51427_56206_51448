from rest_framework import serializers
from .models import Borrowing, User, Book

class BorrowingSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(write_only=True)  # Accept email for user lookup
    book_id = serializers.UUIDField(write_only=True)      # Accept ID for book lookup

    class Meta:
        model = Borrowing
        fields = '__all__'  # Include return_date

    def validate(self, data):
        # Check if user exists by email
        try:
            data['user'] = User.objects.get(email=data['user_email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        # Check if book exists by ID
        try:
            data['book'] = Book.objects.get(id=data['book_id'])
        except Book.DoesNotExist:
            raise serializers.ValidationError("Book with this ID does not exist.")
        
        # Check if the book is available (not borrowed)
        if data['book'].available == 0:
            raise serializers.ValidationError("This book is not currently available.")

        # If everything is valid, remove temporary fields
        del data['user_email']
        del data['book_id']
        return data
