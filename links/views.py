from django.shortcuts import render
from .serializers import  LinkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_logo_url
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class LinkListCreateAPIView(APIView):
    permission_classes =  [IsAuthenticated]
    def post(self, request):
        print(request.data)
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            # Fetch the logo URL
            logo_url = get_logo_url(request.data['url'])
            serializer.save(profile=request.user.userprofile, logo_url=logo_url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)