from rest_framework import generics
from .models import Testapp
from .serializers import TestappSerializer

class TestappList(generics.ListCreateAPIView):
    queryset = Testapp.objects.all()
    serializer_class = TestappSerializer