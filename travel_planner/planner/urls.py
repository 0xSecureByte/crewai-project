# planner/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.plan_travel, name='plan_travel'),
]
