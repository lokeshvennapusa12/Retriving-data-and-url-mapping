from django.shortcuts import render

from app.models import *
from django.db.models import Q

def display_coustomer(request):
    QSC=Coustomer_details.objects.all()
    QSC=Coustomer_details.objects.filter(name__startswith='L')
    QSC=Coustomer_details.objects.filter(name__endswith='a')
    QSC=Coustomer_details.objects.filter(name__contains='a')
    QSC=Coustomer_details.objects.filter(name__regex='\w{4}')
    QSC=Coustomer_details.objects.filter(age__gt='22')
    QSC=Coustomer_details.objects.filter(age__gte='22')
    QSC=Coustomer_details.objects.filter(age__lt='23')
    QSC=Coustomer_details.objects.filter(age__lte='22')
    QSC=Coustomer_details.objects.all()
    d={'coustomer':QSC}
    return render(request,'display_coustomer.html',d)
    
def display_orders(request):
    QSO=Orders.objects.all().order_by()
    QSO=Orders.objects.filter(order_name__in=['Shirt','Sweatshirt','Pant'])
    QSO=Orders.objects.filter(Q(Coustomer_id='2') | Q(order_name='Shirt'))
    QSO=Orders.objects.filter(Q(Coustomer_id='1') | Q(Coustomer_id='3') | Q(order_name='t-shirt'))
    d={'order':QSO}
    return render(request,'display_orders.html',d)