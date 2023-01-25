from django.shortcuts import render

from app.models import *

def display_coustomer(request):
    QSC=Coustomer_details.objects.all()
    d={'coustomer':QSC}
    return render(request,'display_coustomer.html',d)
    
def display_orders(request):
    QSO=Orders.objects.all().order_by()
    d={'order':QSO}
    return render(request,'display_orders.html',d)