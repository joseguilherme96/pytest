import random
from enum import Enum, auto

class Item(Enum):

    APPLE = auto()
    ORANGE = auto()
    BANANA = auto()
    CHOCOLATE = auto()  
    CANDY = auto()  
    GUM = auto()  
    COFFEE = auto()  
    TEA = auto()  
    SODA = auto()  
    WATER = auto() 

    def __str__(self):  
        return self.name.upper()
    
class ShoppingCart:

    def __init__(self):

        self.items = {}

    def add_item(self, item: Item, price: int | float, quantity: int = 1) -> None:

        if item.name in self.items:

            self.items[item.name]["quantity"] += quantity

        else:

            self.items[item.name] = { "price": price, "quantity": quantity }

    def remove_item(self, item: Item, quantity: int = 1) -> None:

        if item.name in self.items:

            if self.items[item.name]['quantity'] <= quantity:

                del self.items[item.name]

            else:

                self.items[item.name]['quantity'] -= quantity

    def get_total_price(self) -> float:

        total = 0.0
        for item in self.items.values():

            total += item['price'] * item['quantity']

        
        return total
    
    def clear_cart(self) -> None:

        self.items = {}

