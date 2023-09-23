from rest_framework import serializers
from measurement.models import Sensor, Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'date']
    
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
        

class MeasurementForSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date', 'image']
        
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementForSensorSerializer(read_only=True, many=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']