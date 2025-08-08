from django.shortcuts import render # Import render to return an html response.
from django.conf import settings # Import project settings.

# View to render the homepage and display the restaurant name.
def homepage(request):
    # Get the restaurant name from settings.py. If not found use the default name "My Restaurant".
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    # Render the 'index.html' template inside 'home' folder and passing the restaurant name as context.
    return render(request, 'home/index.html', {'restaurant_name':restaurant_name})

# View to render the about page and display a brief description and an image of the restaurant.
def about(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    # Render the 'about.html' template inside 'home' folder and passing the restaurant name as context.
    return render(request, 'home/about.html', {'restaurant_name': restaurant_name})



def menu_items(request):
    item_list = ['Pizza','Pasta','Burger','Salad']
    return render(request, 'home/menu.html', {'menu':menu})