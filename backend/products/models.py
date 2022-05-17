from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self): #se puede poner en los fields del serializer
        return "%.2f" %(float(self.price) * 0.8) # calculos de propiedades sin transformar

    def get_discount(self):
        return  "122"