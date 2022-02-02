from django import forms

from .models import product

# creating a form
class EditproForm(forms.ModelForm):
 
    # create meta class
    class Meta:
      # specify model to be used
      #  this line to use model
      model = product
 
        # specify fields to be used
      fields = [
            "name",
            "kind",
            "description",
            "price",
            "expir_date",
        ]

        

 
   

