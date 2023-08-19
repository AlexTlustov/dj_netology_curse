from typing import Iterable, Optional
from django.db import models
from pytils.translit import slugify

class Phone(models.Model):
    name = models.CharField(max_length=254, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=350, null=False)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, primary_key=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


