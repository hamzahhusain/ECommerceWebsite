from django.db import models
from django.db.models import F
from ecommerce import constants
from PIL import Image
from django.contrib.auth.models import User
import sys
# Create your models here.
class Item(models.Model):
    class SuperCategoryChoices(models.TextChoices):
        men = constants.ITEM_SUPER_CATEGORY_MEN
        women = constants.ITEM_SUPER_CATEGORY_WOMEN
        boys = constants.ITEM_SUPER_CATEGORY_BOYS
        girls = constants.ITEM_SUPER_CATEGORY_GIRLS
        adult = constants.ITEM_SUPER_CATEGORY_ADULT
        children = constants.ITEM_SUPER_CATEGORY_CHILDREN
        all = constants.ITEM_SUPER_CATEGORY_ALL
    class SubCategoryChoices(models.TextChoices):
        shirts = constants.ITEM_SUB_CATEGORY_SHIRTS
        pants = constants.ITEM_SUB_CATEGORY_PANTS
        shoes = constants.ITEM_SUB_CATEGORY_SHOES
        accessories = constants.ITEM_SUB_CATEGORY_ACCESSORIES
        misc = constants.ITEM_SUB_CATEGORY_MISC
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    superCategory = models.CharField(
        max_length=12,
        choices = SuperCategoryChoices.choices,
        default=SuperCategoryChoices.all
    )
    subCategory = models.CharField(
        max_length=12,
        choices = SubCategoryChoices.choices,
        default = SubCategoryChoices.misc
    )
    price = models.DecimalField(decimal_places=2, max_digits=8)
    sale = models.SmallIntegerField()
    image = models.ImageField( upload_to='items',default='missingItem.png')
    visible = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.SmallIntegerField(default=1)

    def save(self, *args, **kwargs):
        duplicateCart = Cart.objects.filter(user=self.user.id, item=self.item.id)
        if(len(duplicateCart)==0):
            super().save(*args, **kwargs)
        else:
            newCount=duplicateCart.first().count+self.count
            duplicateCart.update(count=newCount)
        
    
    def __str__(self):
        return self.user.username+" : "+ self.item.name+"("+str(self.count)+")"

