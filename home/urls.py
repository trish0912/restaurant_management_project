from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('menu/', menu_items, name='menu'),
    path('contact/', contact, name='contact'),
    path('reservations/', reservations_view, name='reservations'),
    path('feedback/', feedback_view, name='feedback'),
]