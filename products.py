class Product:
    def __init__(self, name, price, quantity):
        # Initialize the product.
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid values for name, price, or quantity.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity of the product and deactivates if quantity is 0."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Simulates the purchase of a product and updates the quantity."""
        if quantity < 0:
            raise ValueError("Cannot purchase a negative quantity.")
        if quantity > self.quantity:
            raise Exception("Not enough stock to complete the purchase.")

        total_price = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()  # Deactivate product if quantity reaches 0

        return total_price


# Example usage:
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())

