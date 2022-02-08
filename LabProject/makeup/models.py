from audioop import reverse
from django.db import models

# Create your models here.

class brand(models.Model):
    name = models.CharField(max_length=63)
    orign= models.CharField(max_length=63)

    def __str__(self):
        return self.name

    def get_absolate_url(self,Url):
        return reverse("product")
        return self.Url
 # startups = models.ManyToManyField(Startup, related_name = 'blog_posts',null=True)



class product(models.Model):
     name = models.CharField(max_length=63,null=True)
     kind = models.CharField(max_length=63,null=True)
     description=models.CharField(max_length=63,null=True)
     expir_date = models.DateField(null=True)
     price = models.IntegerField(null=True)
     brand=models.ForeignKey(brand, on_delete=models.CASCADE,null=True)
     field_name = models.ImageField(upload_to='static/images/',default='SOME STRING')
