from django.db import models

from django_resized import ResizedImageField


class Item(models.Model):
    """ Модель товара """
    title = models.CharField(max_length=128, null=False, unique=True)
    description = models.TextField(max_length=256, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = ResizedImageField(
        size=[600, 800], crop=['middle', 'center'],
        upload_to='items_photo',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# class Order(models.Model):
#     """ Модель заказа """
#     first_name = models.CharField(max_length=128, null=False, unique=True)
#     last_name = models.CharField(max_length=128, null=False, unique=True)
#     email = models.EmailField(null=False)
#     date = models.DateTimeField(auto_now_add=True, blank=True)
#     items = models.ManyToManyField(Item)

#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
