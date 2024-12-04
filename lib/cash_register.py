#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0
        self.last_transaction_quantity = 0
        self.last_item = None

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.last_transaction_quantity = quantity
        self.last_item = title

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items and self.last_transaction_quantity > 0:
            for _ in range(self.last_transaction_quantity):
                self.items.remove(self.last_item)
            self.total -= self.last_transaction
        else:
            self.total = 0
        self.last_transaction = 0
        self.last_transaction_quantity = 0
        self.last_item = None

    def get_item_price(self, title):
        item_prices = {
            "eggs": 1.99,
            "tomato": 1.76,
            "cheese": 4.5,
            "bread": 4.00,
            "avocado": 1.50
        }
        return item_prices.get(title, 0)
        

      

    
    
    
