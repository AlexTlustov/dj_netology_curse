from django.urls import path
from measurement.views import SensorViewCreate, MeasurementView, SensorListView, SensorOneListView, SensorUpdateView


urlpatterns = [
    path('sensors/', SensorViewCreate.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('list/', SensorListView.as_view()),
    path('sensors/<pk>/', SensorOneListView.as_view()),
    path('sensors_update/<pk>/', SensorUpdateView.as_view())
]