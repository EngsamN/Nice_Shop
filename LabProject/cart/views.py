from traceback import format_exception
from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart(request): 
     ''' create obj cart and get sum of product in cart table '''
     cart_obj =Cart.objects.new_or_get(request)
     # new_obj =Cart.objects.new_or_get(request)

     # producart = cart_obj.products.all()
     # total=0
     # for pro in producart:
     #      total+=pro.price
     # print(total)
     template_name='cart.html'
     return render(request, template_name,{})
     
       