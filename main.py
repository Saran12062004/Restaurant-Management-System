from menu.menu_management import add_menu_item, view_menu
from orders.order_processing import place_order, view_orders
from reservations.reservation_system import add_reservation, view_reservations

def main():
    while True:
        print("\n=== Welcome to the Restaurant Management System ===")
        print("1. Menu Management")
        print("2. Order Processing")
        print("3. Reservations")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            menu_management()
        elif choice == '2':
            order_processing()
        elif choice == '3':
            reservation_system()
        elif choice == '4':
            print("Thank you for using the Restaurant Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def menu_management():
    while True:
        print("\n=== Menu Management ===")
        print("1. Add a new item")
        print("2. View all items")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_menu_item()
        elif choice == '2':
            view_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

def order_processing():
    while True:
        print("\n=== Order Processing ===")
        print("1. Place a new order")
        print("2. View all orders")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            place_order()
        elif choice == '2':
            view_orders()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

def reservation_system():
    while True:
        print("\n=== Reservations ===")
        print("1. Add a reservation")
        print("2. View all reservations")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_reservation()
        elif choice == '2':
            view_reservations()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
