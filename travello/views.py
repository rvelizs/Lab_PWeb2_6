from django.shortcuts import render

from travello.models import Destination
from .models import Destination

# Create your views here.
def index(request):
    
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = "The City That Never Sleeps"
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    
    dest2 = Destination()
    dest2.name = 'Hyderbad'
    dest2.desc = "Fist Biryani, Then Sherwani"
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    
    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = "Beautiful City"
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    
    dests = [dest1, dest2, dest3]
    
    return render(request, "index.html", {'dests' : dests})