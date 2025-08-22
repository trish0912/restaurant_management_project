from django.urls import path
from .views import *

urlpatterns = [
    path('menuitem/', MenuItem_View, name='menuitem'),
    path('menu/', menu_api, name = 'menu_api'),
]