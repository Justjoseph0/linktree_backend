from django.urls import path
from .views import LinkAPIView

urlpatterns = [
    path('links/', LinkAPIView.as_view(), name='links'),
]
