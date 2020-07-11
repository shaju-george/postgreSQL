from django.shortcuts import render

from .models import Destination
# Create your views here.

def index(request ) :

    dest1 = Destination()
    dest1.name = "kerala"
    dest1.desc = "God's own country"
    dest1.img = "destination_1.jpg"
    dest1.price = 7500

    dest2 = Destination()
    dest2.name = "Bangaluru"
    dest2.desc = " City of flowers "
    dest2.img = "destination_2.jpg"
    dest2.price = 6000

    dest3 = Destination()
    dest3.name = "Hydrabad"
    dest3.desc = "Biriyani"
    dest3.img = "destination_3.jpg"
    dest3.price = 5000

    dests = [dest1, dest2, dest3]

    return render (request,'index.html',{'dests':dests})
