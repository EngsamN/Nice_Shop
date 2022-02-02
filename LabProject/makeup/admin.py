from django.contrib import admin
from .models import brand,product
# Register your models here.
admin.site.register(brand)
admin.site.register(product)


class PostAdmin(admin.ModelAdmin):
   list_display={"kind"} 

admin.site.site_header="Cosmetic Boutique Adminstration" 
