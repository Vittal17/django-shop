from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)  # use URLs to avoid media setup
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name