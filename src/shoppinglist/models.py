from django.db import models
from shoppinglist.interfaces import (
    IShoppingList,
    IShoppingLists,
    IProduct,
    IRecipe,
)
from zope.interface import implementer


@implementer(IShoppingLists)
class ShoppingLists(models.Model):
    """DB model for shopping lists."""
    lists = models.ForeignKey('Shopping list')


@implementer(IProduct)
class Product(models.Model):
    """DB model for single product."""
    name = models.CharField(max_length=100)


@implementer(IShoppingList)
class ShoppingList(models.Model):
    """DB model for single shopping list."""
    products = models.ForeignKey(Product)
    created = models.DateTimeField()


@implementer(IRecipe)
class Recipe(models.Model):
    """DB model for recipe."""
    products = models.ForeignKey(Product)
