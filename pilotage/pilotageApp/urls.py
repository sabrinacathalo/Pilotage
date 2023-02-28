from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('synchroData', views.synchroData, name='synchroData'),
    path('dashboard', views.dashboard, name='dashboard')
]