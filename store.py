from typing import List, Tuple
import products


class Store:
    def __init__(self, product_list: List[products.Product]):
        """Initialize the store with a list of products."""
        self.products = product_list  # list of products

    def add_product(self, product: products.Product):
        """Adds a new product to the store."""
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """Removes a product from the store."""
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in store.")

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all active products in the store."""
        total_quantity = sum(product.get_quantity() for product in self.products if product.is_active())
        return total_quantity

    def get_all_products(self) -> List[products.Product]:
        """Returns a list of all active products."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        """Processes an order and calculates the total price."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.is_active():
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Product {product.name} is not available for purchase.")
        return total_price


# Example Usage:
if __name__ == "__main__":
    # Create some products
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)

    products = store.get_all_products()

    print(f"Total quantity of products in store: {store.get_total_quantity()}")

    # make an order
    order_price = store.order([(products[0], 1), (products[1], 2)])
    print(f"Order cost: {order_price} dollars.")
