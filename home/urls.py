from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('history/', about_restaurant, name='history'),
    path('menu/', menu_items, name='menu'),
    path('contact/', contact, name='contact'),
    path('contactform/', contactform, name='contactform'),
    path('reservations/', reservations_view, name='reservations'),
    path('feedback/', feedback_view, name='feedback'),
    path('items/', cart_items, name='items'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

]