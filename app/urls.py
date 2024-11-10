from django.urls import path
from .views import (
    pollutant_list_create,
    pollutant_retrieve_update_delete,
    enterprise_list_create,
    enterprise_retrieve_update_delete
)

urlpatterns = [
    path('pollutants/', pollutant_list_create, name='pollutant_list_create'),
    path('pollutants/<int:id>/', pollutant_retrieve_update_delete, name='pollutant_retrieve_update_delete'),

    path('enterprises/', enterprise_list_create, name='enterprise_list_create'),
    path('enterprises/<int:id>/', enterprise_retrieve_update_delete, name='enterprise_retrieve_update_delete'),
]
