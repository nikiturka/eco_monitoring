from django.urls import path
from . import views

urlpatterns = [
    # Pollutant URLs
    path('pollutants/', views.PollutantListView.as_view(), name='pollutant_list'),
    path('pollutants/create/', views.PollutantCreateView.as_view(), name='pollutant_create'),
    path('pollutant/<int:pk>/', views.PollutantDetailView.as_view(), name='pollutant_detail'),
    path('pollutants/<int:pk>/update/', views.PollutantUpdateView.as_view(), name='pollutant_update'),
    path('pollutants/<int:pk>/delete/', views.PollutantDeleteView.as_view(), name='pollutant_delete'),

    # Enterprise URLs
    path('enterprises/', views.EnterpriseListView.as_view(), name='enterprise_list'),
    path('enterprises/create/', views.EnterpriseCreateView.as_view(), name='enterprise_create'),
    path('enterprises/<int:pk>/', views.EnterpriseDetailView.as_view(), name='enterprise_detail'),
    path('enterprises/<int:pk>/update/', views.EnterpriseUpdateView.as_view(), name='enterprise_update'),
    path('enterprises/<int:pk>/delete/', views.EnterpriseDeleteView.as_view(), name='enterprise_delete'),

    # Record URLs
    path('records/', views.RecordListView.as_view(), name='record_list'),
    path('records/create/', views.RecordCreateView.as_view(), name='record_create'),
    path('records/<int:pk>/', views.RecordDetailView.as_view(), name='record_detail'),
    path('records/<int:pk>/update/', views.RecordUpdateView.as_view(), name='record_update'),
    path('records/<int:pk>/delete/', views.RecordDeleteView.as_view(), name='record_delete'),

    # Home URL
    path('', views.home, name='home'),
]
