from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
  image_url = serializers.SerializerMethodField()

  class Meta:
    model = Book
    fields = ['id', 'title', 'author', 'image', 'image_url', 'year_published', 'category', 'description']

  def get_image_url(self, obj):
    if obj.image:
        return self.context['request'].build_absolute_uri(obj.image.url)
    return None