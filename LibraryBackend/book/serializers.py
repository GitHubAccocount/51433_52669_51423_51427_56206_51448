from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
  image_url = serializers.SerializerMethodField()

  class Meta:
    model = Book
    fields = '__all__'

  def get_image_url(self, obj):
    if obj.image:
        return self.context['request'].build_absolute_uri(obj.image.url)
    return None