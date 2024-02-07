from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    image=models.ImageField(upload_to='amazon_product/',null=True,blank=True)

    def __str__(self):
        return self.title


    @classmethod
    def product_list(self):

       return self.objects.all()

    @classmethod
    def product_details(self,id):
        return self.objects.get(id=id)
