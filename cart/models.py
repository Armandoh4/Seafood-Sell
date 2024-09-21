from django.db import models

# Create your models here.
from products.models import *
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=1,null=True,related_name="products")
    loged_user=models.ForeignKey(User,on_delete=models.CASCADE,default=1,null=True,related_name="User")

    def __str__(self) -> str:
        return self.product.product_name
# f'Customer Email: {customer_email}',
#           f'Amount: {amount_total}',
#           f'Payment Intent: {payment_intent}')

class Record(models.Model):
    customer_email= models.CharField(max_length=3000,null=True,blank=True)
    amount_total= models.CharField(max_length=3000,null=True,blank=True)
    payment_intent= models.CharField(max_length=3000,null=True,blank=True)
    payment_id = models.CharField(max_length=3000,null=True,blank=True)
    status = models.CharField(max_length=3000,null=True,blank=True)

    def __str__(self) -> str:
        return self.customer_email