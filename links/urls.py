from django.urls import path
from .views import LinkListCreateAPIView

urlpatterns = [
    path('links/', LinkListCreateAPIView.as_view(), name='links'),
]
