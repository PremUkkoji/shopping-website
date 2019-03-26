from django import forms
from djongo import models
from PIL import Image
from .fields import MongoDecimalField

class Attributes(models.Model):
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=100)

    class Meta:
        abstract = True


class StockKeepingUnit(models.Model):
    price = MongoDecimalField(max_digits=15, decimal_places=2)
    stock = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Product(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    attributes = models.EmbeddedModelField(
        model_container = Attributes,
    )
    sku = models.EmbeddedModelField(
        model_container = StockKeepingUnit,
    )
    image = models.ImageField(default='default_product.jpg', upload_to='products')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    objects = models.DjongoManager()