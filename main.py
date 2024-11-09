import store
import products


def start(store_obj):
    while True:
        # display menu
        print("\nWelcome to the Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # get user choice
        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            # list all products in store
            all_products = store_obj.get_all_products()
            if all_products:
                print("\nAvailable products in store:")
                for product in all_products:
                    print(f"{product.name} - Price: ${product.price}, Quantity: {product.get_quantity()}")
            else:
                print("\nNo active products in the store.")

        elif choice == "2":
            # total amount in store
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal quantity of products in the store: {total_quantity}")

        elif choice == "3":
            # make an order
            shopping_list = []
            while True:
                print("\nEnter product name and quantity (or type 'done' to finish):")
                product_name = input("Product name: ").strip()
                if product_name.lower() == "done":
                    break

                # find product by name
                product = next((p for p in store_obj.get_all_products() if p.name.lower() == product_name.lower()),
                               None)
                if not product:
                    print(f"Product '{product_name}' not found. Please try again.")
                    continue

                # get quantity
                try:
                    quantity = int(input(f"Quantity for {product_name}: "))
                    if quantity <= 0:
                        print("Please enter a positive quantity.")
                        continue
                except ValueError:
                    print("Invalid quantity. Please enter a valid number.")
                    continue

                shopping_list.append((product, quantity))

            # place order
            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"\nTotal price of your order: ${total_price}")
                except ValueError as e:
                    print(f"Error: {e}")

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
