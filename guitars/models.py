from django.db import models
from django.core.exceptions import ValidationError
class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50, blank=True, null=True, default=None)
    type = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avatar = models.ImageField(upload_to='guitars/avatars/', blank=True, null=True, default=None)
    description = models.TextField(max_length=500, blank=True, null=True, default=None)
    def clean(self):
        if self.year is None or self.year < 1900 or self.year > 2100:
            raise ValidationError('Year must be between 1900 and 2100.')
        if self.price is None or self.price < 0:
            raise ValidationError('Price must be a positive number.')
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"