from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from . import models,serializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
      return render(request, 'index.html', {})

class MenuModelView(generics.ListCreateAPIView):
      queryset = models.Menu.objects.all()
      serializer_class = serializers.MenuModelSerializer

class SingleMenuModelView(generics.RetrieveUpdateDestroyAPIView):
      queryset = models.Menu.objects.all()
      serializer_class = serializers.MenuModelSerializer

class BookingModelView(ModelViewSet):
      queryset = models.Booking.objects.all()
      serializer_class = serializers.BookingModelSerializer
      permission_classes = [IsAuthenticated]