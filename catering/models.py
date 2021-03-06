from django.db import models
from django.urls import reverse

from meals.models import get_slug


class CateringCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Catering Category'
        verbose_name_plural = 'Catering Categories'

    def __str__(self):
        return f'{self.name}'


class CateringProduct(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(CateringCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='catering_product/', null=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Catering Product'
        verbose_name_plural = 'Catering Products'

    def get_absolute_url(self):
        return reverse('catering:catering_product_details_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
