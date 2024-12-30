import os
from menu.discount_decorator import apply_discount

def place_order():
    # Check if the menu file exists and has content
    if not os.path.exists("data/menu.txt") or os.path.getsize("data/menu.txt") == 0:
        print("No menu items available to order.")
        return

    # Read the menu file
    with open("data/menu.txt", "r") as file:
        menu = file.readlines()

    # Display the menu to the user
    print("\n=== Menu ===")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item.strip()}")

    try:
        # Take order input from the user
        order_numbers = input("Enter menu item numbers separated by commas (e.g., 1,3): ")
        order_indices = [int(num.strip()) - 1 for num in order_numbers.split(",")]

        # Validate the indices
        if any(index < 0 or index >= len(menu) for index in order_indices):
            print("Invalid menu item number(s). Please try again.")
            return

        # Get the ordered items
        order_items = [menu[i].strip() for i in order_indices]

    except (ValueError, IndexError):
        print("Invalid input. Please enter valid menu item numbers separated by commas.")
        return

    @apply_discount(10)
    def calculate_total():
        total = 0
        for item in order_items:
            # Extract the price from the menu item (e.g., "Burger - $5.99")
            price = float(item.split("$")[1])
            total += price
        return total

    # Calculate the total price with a discount
    total = calculate_total()

    # Save the order in the orders.txt file
    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/orders.txt", "a") as file:
        file.write(f"Order: {', '.join(order_items)} | Total: ${total:.2f}\n")

    # Display order details to the user
    print("\nOrder placed successfully!")
    print(f"Order Details:")
    for item in order_items:
        print(f"- {item}")
    print(f"Total (after discount): ${total:.2f}")

def view_orders():
    # Check if the orders file exists and has content
    if not os.path.exists("data/orders.txt") or os.path.getsize("data/orders.txt") == 0:
        print("No orders found.")
        return

    # Read and display all orders
    with open("data/orders.txt", "r") as file:
        print("\n=== All Orders ===")
        for line in file:
            print(line.strip())
