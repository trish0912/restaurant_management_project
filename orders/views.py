from django.shortcuts import render
from .models import MenuItem

# Create your views here.

def MenuItem_View(request):
    try:
        all_items = MenuItem.objects.all()
    except Exception as e:
        all_items = []
        print(f"Error fetching menu items: {e}")

    return render(request, 'orders/menu_item.html', {'all_items':all_items})
    
