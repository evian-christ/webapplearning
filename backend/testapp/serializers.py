from rest_framework import serializers
from .models import Testapp

class TestappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testapp
        fields = ['id', 'title', 'content']