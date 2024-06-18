from django.urls import path
from .views import TestappList

urlpatterns = [
    path('testapp/', TestappList.as_view(), name='testapp-list'),
]