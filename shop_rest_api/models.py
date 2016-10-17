import json

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

RATING_CHOICES = [(i, j) for i, j in enumerate(range(1, 6), start=1)]


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)  # product name
    description = models.TextField(blank=True)  # product description
    attributes = models.TextField(blank=True)  # product attributes in JSON format
    images = models.URLField()  # product image url

    def clean(self):
        try:
            json.loads(self.attributes)
        except ValueError:
            raise ValidationError("attributes field must be valid JSON")


    def __str__(self):
        return "%s Item" % self.name


class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField(blank=False)
    rating = models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    approved = models.BooleanField(default=False)

    def __str__(self):
        return "%s's review on item %s " % (self.author_name, self.item)




