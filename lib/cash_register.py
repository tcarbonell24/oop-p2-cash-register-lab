#!/usr/bin/env python3

class CashRegister:
    '''
    A simple Cash Register model that allows adding items, applying discounts,
    and voiding the last transaction.
    '''

    def __init__(self, discount=0):
        '''
        Initialize a new CashRegister.
        Arguments:
            discount (int): Optional discount percentage (0–100). Defaults to 0.
        '''
        self.discount = discount if discount else 0
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        '''
        Add an item (or multiple of the same item) to the register.
        Updates total, items list, and previous_transactions log.
        '''
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        '''
        Apply the discount to the total if one exists.
        Prints the new total after discount, or an error message if none exists.
        '''
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            # Tests expect integers, not floats
            self.total = int(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        '''
        Remove the last transaction from the register, updating total and items.
        If no transactions exist, nothing happens.
        '''
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])
