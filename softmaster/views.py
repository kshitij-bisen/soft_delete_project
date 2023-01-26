# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Color
from .serializers import ColorSerializer
# Create your views here.


class ColorView(APIView):
    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        if serializer is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NonDeletedColorView(APIView):
    def get(self, request):
        colors = Color.color_obj.all()
        serializer = ColorSerializer(colors, many=True)
        if serializer is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
