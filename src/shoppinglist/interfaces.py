from zope.interface import (
    Interface,
    Attribute,
)


class IShoppingLists(Interface):
    """Marker interface for Shopping Lists."""
    lists = Attribute("list")


class IShoppingList(Interface):
    """Marker interface for Shopping list."""
    products = Attribute("products", "List of products.")
    created = Attribute("created", "Creation date and time.")


class IProduct(Interface):
    """Marker interface for Product."""
    name = Attribute("name", "Product name")


class IRecipe(Interface):
    """Marker interface for Recipe."""
    name = Attribute("name", "Recipe name")
    description = Attribute("description",
                            "Recipe description")
    products = Attribute("products",
                         "List of ingredients.")
