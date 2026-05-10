class Bus:

    def __init__(self, number,route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

        def available_seats(self):
            return self.total_seats - self.booked_seats

        def book_seat():
            if self.available_seats() > 0:
                self.booked_seats += 1
                return True
            else:
                return False
    
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
        