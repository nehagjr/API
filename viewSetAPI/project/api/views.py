from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SnippetSerializer
from .models import Snippet
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
