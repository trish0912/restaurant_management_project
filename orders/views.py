from django.shortcuts import render
from .models import MenuItem
from rest_framework.decorators import api_view
from rest_framework.response import Response



# View to render Menu Items
def MenuItem_View(request):
    try:
        all_items = MenuItem.objects.all()
    except Exception as e:
        all_items = []
        print(f"Error fetching menu items: {e}")

    return render(request, 'orders/menu_item.html', {'all_items':all_items})



# View to retrieve restaurant's menu- Restaurant Menu API
@api_view(['GET'])
def menu_api(request):
    menu = [
        {
            'name':'Margherita Pizza',
            'description':'Classic cheese and tomato pizza',
            'price':299
        },
        {
            'name':'Pasta Alfredo',
            'description':'Creamy pasta with garlic and cheese sauce',
            'price':399
        }
    ]

    return Response(menu)
    
