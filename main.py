import store
import products


def show_menu():
    """Displays the main menu."""
    print("\nWelcome to the Store!")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_obj):
    """Lists all products in the store."""
    all_products = store_obj.get_all_products()
    if all_products:
        print("\nAvailable products in store:")
        for idx, product in enumerate(all_products, start=1):
            print(f"{idx}. {product.name} - Price: ${product.price}, Quantity: {product.get_quantity()}")
    else:
        print("\nNo active products in the store.")


def show_total_quantity(store_obj):
    """Shows the total quantity of products in the store."""
    total_quantity = store_obj.get_total_quantity()
    print(f"\nTotal quantity of products in the store: {total_quantity}")


def make_order(store_obj):
    """Handles making an order."""
    shopping_list = []
    while True:
        print("\nEnter the product index and quantity (or type 'done' to finish):")
        product_idx = input("Product index: ").strip()

        if product_idx.lower() == 'done':
            break

        # validate index
        try:
            product_idx = int(product_idx) - 1  # adjust index to zero-based
            all_products = store_obj.get_all_products()
            if product_idx < 0 or product_idx >= len(all_products):
                print("Invalid product index. Please try again.")
                continue
            product = all_products[product_idx]
        except ValueError:
            print("Invalid input. Please enter a valid product index.")
            continue

        # get quantity
        try:
            quantity = int(input(f"Quantity for {product.name}: "))
            if quantity <= 0:
                print("Please enter a positive quantity.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
            continue

        shopping_list.append((product, quantity))

    # place the order
    if shopping_list:
        try:
            total_price = store_obj.order(shopping_list)
            print(f"\nTotal price of your order: ${total_price}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


def start(store_obj):
    """Main loop of the store program."""
    while True:
        show_menu()
        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total_quantity(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)

    start(best_buy)
