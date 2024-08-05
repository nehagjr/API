from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentList.as_view())
]