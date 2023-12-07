from rest_framework import serializers
from books import models

class BooksSerializer(serializers.ModelSerializer):
    class meta:
        model = models.Books
        fields = '__all__'