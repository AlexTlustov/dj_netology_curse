from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from rest_framework.response import Response
from rest_framework import serializers
from django.forms import model_to_dict
from django.utils import timezone


class SensorViewCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorOneListView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    
class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer