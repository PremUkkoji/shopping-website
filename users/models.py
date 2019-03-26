from djongo import models
from django import forms
from django.contrib.auth.models import User
from products.models import Product
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_user.jpg', upload_to='users')
    purchased = models.ManyToManyField(Product, related_name = 'purchased', blank=True)
    cart = models.ManyToManyField(Product, related_name = 'cart', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    objects = models.DjongoManager()