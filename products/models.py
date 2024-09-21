from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
    def clean(self):
        if self.price <= 0:
            raise ValidationError('Price must be greater than 0.')

    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean method
        super(Product, self).save(*args, **kwargs)

class Product_images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=1,null=True,related_name="productimg")
    image = models.ImageField(upload_to="images", null=True,blank=True)
    def __str__(self) -> str:
        return self.product.product_name
