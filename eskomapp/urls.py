# eskomapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('search/', views.search, name='search'),
    path('area_info/<str:area_id>/', views.area_info, name='area_info'),
]
