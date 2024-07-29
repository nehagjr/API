from django.urls import path
from .views import *
urlpatterns = [
    path('student/', student),
    path('studentlink/', studentlink)
]