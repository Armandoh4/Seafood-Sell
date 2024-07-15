from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    categorie=models.CharField(max_length=1300,null=True)
    def __str__(self) -> str:
        return self.categorie


class Product(models.Model):
    product_name = models.CharField(max_length=3000)
    price = models.IntegerField()
    description=models.TextField()
    Categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,default=1,null=True)
    def __str__(self) -> str:
        return self.product_name

class Product_images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=1,null=True,related_name="productimg")
    image = models.ImageField(upload_to="images", null=True,blank=True)
    def __str__(self) -> str:
        return self.product.product_name

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=1,null=True,related_name="products")
    loged_user=models.ForeignKey(User,on_delete=models.CASCADE,default=1,null=True,related_name="User")

    def __str__(self) -> str:
        return self.product.product_name
# f'Customer Email: {customer_email}',
#           f'Amount: {amount_total}',
#           f'Payment Intent: {payment_intent}')

class Record(models.Model):
    customer_email= models.CharField(max_length=3000)
    amount_total= models.CharField(max_length=3000)
    payment_intent= models.CharField(max_length=3000)


    def __str__(self) -> str:
        return self.customer_email