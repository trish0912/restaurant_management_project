from django.shortcuts import redirect, render # Import render to return an html response.
from django.conf import settings # Import project settings.
from django.db import DatabaseError
import logging
from .forms import FeedbackForm, ContactMessageForm

"""
logger = logging.getLogger(__name__) - is how django (and python) creates a logger instance
that is tied to the name of the current python module.
"""
logger = logging.getLogger(__name__)

# View to render the homepage and display the restaurant name.
def homepage(request):
    try:
        # Get the restaurant phone number from settings.py. Default value is not applicable. 
        restaurant_phone = getattr(settings, 'RESTAURANT_PHONE', 'N/A')
        # Get the restaurant name from settings.py. If not found use the default name "My Restaurant".
        restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
        # Render the 'index.html' template inside 'home' folder and passing the restaurant name as context.
        error_message = None
    except (DatabaseError, Exception) as e:
        logger.error(f"Error loading homepage data: {e}")
        restaurant_phone = 'N/A'
        restaurant_name = 'My Restaurant'
        error_message = "Some information could not be loaded. Please try again later."

        return render(request, 'home/index.html', {'restaurant_name':restaurant_name, 'restaurant_phone': restaurant_phone, 'error_message':error_message})

# View to render the about page and display a brief description and an image of the restaurant.
def about(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    # Render the 'about.html' template inside 'home' folder and passing the restaurant name as context.
    return render(request, 'home/about.html', {'restaurant_name': restaurant_name})


# View to render menu items
def menu_items(request):
    item_list = ['Pizza','Pasta','Burger','Salad']
    return render(request, 'home/menu.html', {'menu':menu})

# View to render contact us page
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactMessageForm()
    return render(request, 'home/contact.html', {'form':form})

# View to render reservation page
def reservations_view(request):
    return render(request, 'home/reservations.html')

# View to render feedback page
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'home/feedback.html', {'form':form})


def index(request):
    """
    Homepage view.
    This view fetches menu data from the restaurant's API(orders app)
    and pass it to index.html template to display
    """
    try:
        response = requests.get("http://127.0.0.1:8000/api/orders/menu/")