class ShoppingCart:
    tax_rate = 0.08

    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        """Add an item to shopping cart."""
        self.items.append({'name':name, 'price': price})

    
    def calculate_total(self):
        """Calculate the total price including tax."""
        total = sum(item['price'] for item in self.items)
        total_with_tax = total + (total * self.tax_rate)
        return total_with_tax

    def apply_discont(self, discount_percentage):
        """Apply a discount to the total price."""
        total = self.calculate_total()
        discount = total * (discount_percentage / 100)
        return total - discount


    @staticmethod
    def format_price(amount):
     """ Format the price to two decimal places."""
     return f"${amount:.2f}"

    @staticmethod

    def calculate_tax(amount):
        """calculate tax for a given amount."""
        return amount * ShoppingCart.tax_rate

#example usage:

cart = ShoppingCart()
cart.add_item("laptop",10000)
cart.add_item("ear buds", 2000)
cart.add_item("mouse",1500)

#Calculate the total price
total_price = cart.calculate_total()
print(F"Total price (including tax): {ShoppingCart.format_price(total_price)}")

#Apply a discount
discounted_price = cart.apply_discont(10)
print(F"price after discount: {ShoppingCart.format_price(discounted_price)}")

#Calculate the tax on a apecific amount
tax_on_laptop = ShoppingCart.calculate_tax(1000)
print(F"tax on laptop:- {ShoppingCart.format_price(tax_on_laptop)}")