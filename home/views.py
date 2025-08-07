from django.shortcuts import render # Import render to return an html response
from django.conf import settings # Import project settings

# View to render the homepage and display the restaurant name
def homepage(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    return render(request, 'home/index.html', {'restaurant_name':restaurant_name})