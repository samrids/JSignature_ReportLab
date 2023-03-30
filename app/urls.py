from __future__ import unicode_literals

from django.contrib import admin
from django.urls import path

from app import views








urlpatterns = [
    path('', views.ExampleListView.as_view(), name='list'),
    path('create', views.ExampleCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.ExampleUpdateView.as_view(), name='update'),

    path('generate_pdf/<int:id>', views.generate_pdf, name='generate_pdf'),


    
]