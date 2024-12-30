import os

def add_menu_item():
    item_name = input("Enter item name: ")
    while True:
        try:
            item_price = float(input("Enter item price: "))
            break
        except ValueError:
            print("Invalid price. Please enter a valid number.")

    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/menu.txt", "a") as file:
        file.write(f"{item_name} - ${item_price:.2f}\n")
    print(f"Item '{item_name}' added to the menu.")

def view_menu():
    if not os.path.exists("data/menu.txt") or os.path.getsize("data/menu.txt") == 0:
        print("No menu items found.")
        return

    with open("data/menu.txt", "r") as file:
        print("\n=== Menu ===")
        for line in file:
            print(line.strip())
