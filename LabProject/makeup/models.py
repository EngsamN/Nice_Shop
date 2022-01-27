from django.db import models

# Create your models here.

class brand(models.Model):
    Name = models.CharField(max_length=63)
    Orign=models.CharField(max_length=63)

    def __str__(self):
        return self.Name

    def get_absolate_url(self,Url):
        return self.Url
 # startups = models.ManyToManyField(Startup, related_name = 'blog_posts',null=True)



class product(models.Model):
     Name = models.CharField(max_length=63)
     kind = models.CharField(max_length=63)
     description=models.CharField(max_length=63)
     Expir_date = models.DateField()
     price = models.IntegerField()
     brand=models.ForeignKey(brand, on_delete=models.CASCADE)