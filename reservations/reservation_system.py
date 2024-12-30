import os

def generate_reservation_id(last_id=1000):
    if os.path.exists("data/reservations.txt"):
        with open("data/reservations.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_id = int(last_line.split("|")[0].strip()[1:])
    return f"R{last_id + 1}"

def add_reservation():
    customer_name = input("Enter customer name: ")
    party_size = input("Enter party size: ")

    reservation_id = generate_reservation_id()
    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/reservations.txt", "a") as file:
        file.write(f"{reservation_id} | {customer_name} | Party Size: {party_size}\n")
    print(f"Reservation ID: {reservation_id}")
    print(f"Reservation for '{customer_name}' added successfully!")

def view_reservations():
    if not os.path.exists("data/reservations.txt") or os.path.getsize("data/reservations.txt") == 0:
        print("No reservations found.")
        return

    with open("data/reservations.txt", "r") as file:
        print("\n=== All Reservations ===")
        for line in file:
            print(line.strip())
