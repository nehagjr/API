from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SnippetSerializer
from .models import Snippet
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()