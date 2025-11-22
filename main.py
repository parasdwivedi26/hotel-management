class Customer:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.room_number = 0

    def input_data1(self):
        print("________________________________________________________________")
        print("\t\t Room Booking Portal                           ")
        print("________________________________________________________________")
        self.name = input("Enter your Name                       \t : ")
        self.address = input("Enter your Address                    \t : ")
        while True:
            try:
                self.room_number = int(input("Enter any Room Number                \t : "))
                if self.room_number <= 0:
                    print("Room number must be positive.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid room number.")


class Room:
    ROOM_TYPES = {
        1: {"name": "AC, Large", "rate": 10000},
        2: {"name": "AC, Small", "rate": 8000},
        3: {"name": "Non-AC, Large", "rate": 4000},
        4: {"name": "Non-AC, Small", "rate": 3000},
    }

    def __init__(self):
        self.room_type = 0
        self.days = 0

    def input_data2(self):
        print("\n\t\t Available Room Types                     ")
        print("\n\t1. Type : A/C; Size : Large; Rate : 10000")
        print("\t2. Type : A/C; Size : Small; Rate : 8000")
        print("\t3. Type : Non A/C; Size : Large; Rate : 4000")
        print("\t4. Type : Non A/C; Size : Small; Rate : 3000\n")

        while True:
            try:
                room_type_input = int(input("Enter Your Room Type (1-4)         \t: "))
                if room_type_input in Room.ROOM_TYPES:
                    self.room_type = room_type_input
                    break
                else:
                    print("Invalid room type. Please enter 1-4.")
            except ValueError:
                print("Invalid input. Please enter 1-4.")

        while True:
            try:
                self.days = int(input("For how many days will you stay?     : "))
                if self.days <= 0:
                    print("Days must be positive.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter days as integer.")

    def calculate_rent(self):
        if self.room_type in Room.ROOM_TYPES:
            room_info = Room.ROOM_TYPES[self.room_type]
            return room_info["rate"] * self.days
        else:
            print("Room type not set correctly.")
            return 0


class Restaurant:
    MENU = {
        1: {"item": "Water", "price": 20},
        2: {"item": "Tea", "price": 50},
        3: {"item": "Breakfast Combo", "price": 100},
        4: {"item": "Lunch", "price": 400},
        5: {"item": "Dinner", "price": 400},
    }

    def __init__(self):
        self.food_bill = 0

    def order_food(self):
        print("================================================")
        print("\n\t\tRestaurant Menu     ")
        print("\n\t1: Water - 20")
        print("\t2: Tea - 50")
        print("\t3: Breakfast Combo - 100")
        print("\t4: Lunch - 400")
        print("\t5: Dinner - 400")
        print("\t6: Exit")
        print("================================================")

        while True:
            try:
                choice = int(input("Enter your choice (1-5, 6 to exit): "))
            except ValueError:
                print("Invalid input.")
                continue

            if choice == 6:
                break
            elif choice in Restaurant.MENU:
                while True:
                    try:
                        quantity = int(input("Enter the quantity: "))
                        if quantity <= 0:
                            print("Quantity must be positive.")
                        else:
                            break
                    except ValueError:
                        print("Invalid quantity.")
                item_info = Restaurant.MENU[choice]
                self.food_bill += item_info["price"] * quantity
                print(f"Added {quantity} x {item_info['item']}")
            else:
                print("Invalid option.")

    def calculate_bill(self):
        print("\tTotal Food Cost = Rs", self.food_bill)


class TotalBill(Customer, Room, Restaurant):
    def __init__(self):
        Customer.__init__(self)
        Room.__init__(self)
        Restaurant.__init__(self)
        self.totalbill = 0
        self.extracharges = 500

    def calculate_total(self):
        room_rent = self.calculate_rent()
        print("\tRoom Rent            = Rs", room_rent)
        self.calculate_bill()
        print("\tExtra Charges        = Rs", self.extracharges)
        self.totalbill = room_rent + self.food_bill + self.extracharges
        print("\tTotal Bill           = Rs", self.totalbill)


def main():
    customers = []
    booked_rooms = set()

    while True:
        print("==================================================")
        print("\t\tWelcome To CITY HOTEL ")
        print("==================================================")
        print("\t\t1. Book A Room")
        print("\t\t2. Calculate Room Rent")
        print("\t\t3. Order Food")
        print("\t\t4. Show Restaurant Bill")
        print("\t\t5. Show Total Cost")
        print("\t\t6. Show Booked Rooms")
        print("\t\t7. Exit")
        print("________________________________________________________________")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            total = TotalBill()
            total.input_data1()
            if total.room_number not in booked_rooms:
                total.input_data2()
                customers.append(total)
                booked_rooms.add(total.room_number)
                print(f"\n\tRoom No {total.room_number} booked successfully for {total.name}.")
            else:
                print(f"\tRoom No {total.room_number} is already booked.")

        elif choice == 2:
            if not customers:
                print("Please enter customer data first.")
            else:
                total = customers[-1]
                print(f"\tCalculated Room Rent : Rs {total.calculate_rent()}")

        elif choice == 3:
            if not customers:
                print("Please enter customer data first.")
            else:
                customers[-1].order_food()
                print("\n\tFood Ordered Successfully!")

        elif choice == 4:
            if not customers:
                print("Please enter customer data first.")
            else:
                customers[-1].calculate_bill()

        elif choice == 5:
            if not customers:
                print("\tPlease enter customer data first.")
            else:
                total = customers[-1]
                print("\n\t\t RECEIPT ")
                print("========================================")
                print(f"\tCustomer Name        : {total.name}")
                print(f"\tAddress              : {total.address}")
                print(f"\tRoom Number          : {total.room_number}")
                total.calculate_total()
                print("========================================")

        elif choice == 6:
            if booked_rooms:
                print("\tBooked Rooms :", booked_rooms)
            else:
                print("No rooms booked yet.")

        elif choice == 7:
            print("\tCheckout.")
            print("***************************************************************************")
            print("\t\tThank you for visiting CITY HOTEL")
            print("***************************************************************************")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
