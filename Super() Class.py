class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def display(self):
        print (f"item-- {self.name}, Quantity-- {self.quantity}")

class PerishableItem(Item):
    def __init__(self, name, quantity, expiry_date):
        super().__init__(name, quantity)
        self.expiry_date = expiry_date


    def display(self):
        super().display()
        print(F"Expiry Date:- {self.expiry_date}")


class NonperishableItem(Item):
    def display(self):
        super().display()
        print("this is a non- perishable item.")



apple = PerishableItem("apple", 10, "2024-10-23")
mango = NonperishableItem("mango", 23)

print("perishable item details")
apple.display()
print("-------------***-------------")
print(f"\nnon-perishable item details--{mango.display()}")

        