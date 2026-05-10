class Bus:

    def __init__(self, number,route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
                self.booked_seats += 1
                return True
        else:
            return False
    fixed_fare = 500

class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False
    
class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, seats):
        for bus in self.buses:
            if bus.number == number:
                print("Bus Already Added")
                return
        
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print("Bus Added Successfully")

    def show_buses(self):
        if len(self.buses) == 0:
            print("No buses here")
            return
        else:
            print("----- ALL BUSES -----")
            for bus in self.buses:
                print(f"Bus number is: {bus.number} Route is: {bus.route} Total seat: {bus.total_seats} Available seats: {bus.available_seats()}")

    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus.number == bus_number:
                if bus.book_seat():
                    passenger = Passenger(name, phone, bus)
                    self.passengers.append(passenger)
                    print(f"Ticket Booked Successfully")
                else:
                    print("No Seats Available")
                return
        print("Bus Not Found")

system = BusSystem()

admin = Admin('admin', '1234')

while True:
    print("====== Bangladesh Bus Ticket Booking System ======")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")

    choice = input("Enter Your Choice(1-4): ")

    if choice == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if admin.login(username, password):
            print("Login Successful")

            while True:
                print("1. Add Bus")
                print("2. View All Buses")
                print("3. Logout")

                a_choice = input("Enter your choice: ")

                if a_choice == "1":
                    number = input("Enter bus number: ")
                    route = input("Enter bus route: ")
                    try:
                        seats = int(input("Enter total seat: "))
                        if seats <= 0:
                            print("Seate number must be more than 0")
                            continue
                        else:
                            system.add_bus(number, route, seats)
                    except ValueError:
                        print("Invalid seat number")

                elif a_choice == "2":
                    system.show_buses()

                elif a_choice == "3":
                    print("logged out successfully")
                    break
                else:
                    print("Invalid choice")
        
    elif choice == "2":
        bus_number = input("Enter bus number: ")
        name = input("Enter passenger name: ")
        phone = input("Enter phone number: ")

        system.book_ticket(bus_number, name, phone)

    elif choice == "3":
        system.show_buses()

    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")