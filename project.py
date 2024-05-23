import csv
import os
import threading

def read_bus_details():
    buses = []
    file_path = r'C:\Users\user\Desktop\website\bus project\bus.txt'
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            buses.append(row)
    return buses

def read_user_details():
    users = {}
    file_path = r'C:\Users\user\Desktop\website\bus project\users.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                username, password = row
                users[username] = password
    return users

def write_user_details(users):
    file_path = r'C:\Users\user\Desktop\website\bus project\users.txt'
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for username, password in users.items():
            writer.writerow([username, password])

def register_user():
    users = read_user_details()
    username = input("\nEnter a username: ")
    while username in users:
        print("Username already exists. Choose another one.")
        username = input("Enter a username: ")
    password = input("Enter a password: ")
    users[username] = password
    write_user_details(users)
    print("Registration successful. You can now log in.")

def login_user():
    users = read_user_details()
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")
    if users.get(username) == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

def display_available_buses(buses):
    print("\nAvailable Buses:")
    for i, bus in enumerate(buses):
        print(f"{i + 1}. Bus ID: {bus[0]}, Date: {bus[1]}, Time: {bus[2]}")

def display_available_seats(bus):
    print(f"\nBus ID: {bus[0]}, Date: {bus[1]}, Time: {bus[2]}")
    print("\nAvailable Seats:")
    for i, seat in enumerate(bus[3:]):
        if seat == '0':
            print(f"Seat {i + 1}")

def display_reserved_seats(bus):
    print(f"\nBus ID: {bus[0]}, Date: {bus[1]}, Time: {bus[2]}")
    print("\nReserved Seats:")
    for i, seat in enumerate(bus[3:]):
        if seat == '1':
            print(f"Seat {i + 1}")

def reserve_seat(buses, bus_index, seat_number):
    if buses[bus_index][seat_number + 3] == '0':
        buses[bus_index][seat_number + 3] = '1'
        print(f"\nSeat {seat_number + 1} reserved successfully!")
        write_to_file(buses)
    else:
        print("\nSeat already reserved. Please choose another seat.")

def cancel_reservation(buses, bus_index, seat_number):
    if buses[bus_index][seat_number + 3] == '1':
        buses[bus_index][seat_number + 3] = '0'
        print(f"\nReservation for Seat {seat_number + 1} canceled successfully!")
        write_to_file(buses)
    else:
        print("\nSeat is not reserved. Nothing to cancel.")

def write_to_file(buses):
    file_path = r'C:\Users\user\Desktop\website\bus project\bus.txt'
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(buses)

def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            username = login_user()
            if username:
                all_buses = read_bus_details()
                while True:
                    print("\nBus Reservation Menu:")
                    print("4. Display available buses")
                    print("5. Reserve a seat")
                    print("6. Cancel reservation")
                    print("7. Display available seats for a bus")
                    print("8. Display reserved seats for a bus")
                    print("9. Logout")
                    sub_choice = input("Enter your choice (4-9): ")

                    if sub_choice == '4':
                        display_available_buses(all_buses)
                    elif sub_choice == '5':
                        selected_bus_index = int(input("Enter the bus number to reserve a seat: ")) - 1
                        seat_to_reserve = int(input("Enter the seat number to reserve (1-20): ")) - 1
                        reserve_seat(all_buses, selected_bus_index, seat_to_reserve)
                    elif sub_choice == '6':
                        selected_bus_index = int(input("Enter the bus number to cancel a reservation: ")) - 1
                        seat_to_cancel = int(input("Enter the seat number to cancel (1-20): ")) - 1
                        cancel_reservation(all_buses, selected_bus_index, seat_to_cancel)
                    elif sub_choice == '7':
                        selected_bus_index = int(input("Enter the bus number to display available seats: ")) - 1
                        display_available_seats(all_buses[selected_bus_index])
                    elif sub_choice == '8':
                        selected_bus_index = int(input("Enter the bus number to display reserved seats: ")) - 1
                        display_reserved_seats(all_buses[selected_bus_index])
                    elif sub_choice == '9':
                        print("\nLogging out. Goodbye!")
                        break
                    else:
                        print("\nInvalid choice. Please enter a number between 4 and 9.")
        elif choice == '3':
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()