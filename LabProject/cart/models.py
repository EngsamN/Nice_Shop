from django.db import models 
from django.conf import  settings

from makeup.models import product

User =settings.AUTH_USER_MODEL
# Create your models here.

#model manager
''' Adding extra manager methods(custom managers) is the preferred way to add “table-level” functionality to your models whereas for “row-level” functionality use model methods.'''
class CartManager(models.Manager):

    '''function to query about cart item if it exists it will selct it
    else it will creat it '''
    def new_or_get(self,request):
        cart_id=request.session.get("cart_id",None)
        qs=self.get_queryset().filter(id=cart_id)
        if qs.count()==1:
          new_obj=False
          print('Cart ID exists')
          cart_obj=qs.first() #get first object
          if request.user.is_authenticated and cart_obj.user is None:
               cart_obj=request.user
               cart_obj.save()
          else:
              cart_obj=Cart.objects.new(user=request.user)
              new_obj=True
              request.session['cart_id']=cart_obj.id
            #   template_name='cart.html'
          return cart_obj,new_obj

    def new(self,user=None):
        print(user.is_authenticated)
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj=user
        return self.model.objects.create(user=user)



#cart model
class Cart(models.Model):
    user = models.CharField(User,null=True,blank=True,max_length=70) # to be sure any user can create cart
    products= models.ManyToManyField(product,max_length=63,blank=True)
    total= models.DecimalField(default=00.0,max_digits=100,decimal_places=2)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    objects=CartManager()
    def __str__(self):
        return str(self.id)

  