from django.db import models
from django.forms.fields import ImageField


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    
    
    def __set__(self):
        return self.name
    
    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = 'Датчики'

    
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name = 'measurements')
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    
    def __set__(self):
        return str(self.sensor)
    
    class Meta:
        verbose_name = "Измерение"
        verbose_name_plural = 'Измерения'