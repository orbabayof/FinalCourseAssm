from rest_framework.serializers import ModelSerializer
from . import models
class MenuModelSerializer(ModelSerializer):
     class Meta:
          model = models.Menu
          fields = "__all__"

class BookingModelSerializer(ModelSerializer):
     class Meta:
          model = models.Booking
          fields = "__all__"