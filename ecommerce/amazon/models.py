from django.db import models





class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    thumbnail = models.URLField()

    def __str__(self):
        return self.title
