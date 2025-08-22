from django.urls import path
from .views import *

urlpatterns = [
    path('menuitem/', MenuItem_View, name='menuitem'),
    path('api/menu/', )
]