from django.urls import path
from . import views

app_name = 'chart'

urlpatterns = [
    path('', views.songs, name='songs'),
    path('<int:pk>/', views.detail, name='detail'),
]