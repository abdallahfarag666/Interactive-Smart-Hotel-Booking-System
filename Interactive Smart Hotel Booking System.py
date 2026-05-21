from abc import ABC, abstractmethod


# ================= ABSTRACT CLASS =================

class HotelItem(ABC):

    def __init__(self, item_id, name, base_price):

        self.__item_id = item_id
        self.__name = name
        self.__base_price = base_price

    # Getters
    def get_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def get_base_price(self):
        return self.__base_price

    # Setter with validation
    def set_base_price(self, price):

        if price > 0:
            self.__base_price = price

        else:
            print("Invalid price!")

    # Abstract Methods
    @abstractmethod
    def calculate_item_cost(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


# ================= ROOM CLASS =================

class Room(HotelItem):

    def __init__(self, item_id, name, base_price, bed_size):

        super().__init__(item_id, name, base_price)

        self.__bed_size = bed_size

    # Polymorphism
    def calculate_item_cost(self):

        # 15% hotel tax
        return self.get_base_price() * 1.15

    def display_details(self):

        print(f"ID: {self.get_id()}")
        print(f"Room: {self.get_name()}")
        print(f"Bed Size: {self.__bed_size}")
        print(f"Base Price: ${self.get_base_price():.2f}")


# ================= SERVICE CLASS =================

class Service(HotelItem):

    def __init__(self, item_id, name, base_price, duration):

        super().__init__(item_id, name, base_price)

        self.__duration = duration

    # Polymorphism
    def calculate_item_cost(self):

        # 20% gratuity fee
        return self.get_base_price() * 1.20

    def display_details(self):

        print(f"ID: {self.get_id()}")
        print(f"Service: {self.get_name()}")
        print(f"Duration: {self.__duration} mins")
        print(f"Base Price: ${self.get_base_price():.2f}")


# ================= RESERVATION CLASS =================

class CustomerReservation:

    def __init__(self):

        self.items = []

    # Add item
    def add_item(self, item):

        self.items.append(item)

    # Show reservation
    def show_reservation(self):

        if not self.items:

            print("\nReservation is empty.")
            return

        print("\n===== CUSTOMER RESERVATION =====")

        for item in self.items:

            item.display_details()
            print("-------------------------")

    # Print final bill
    def print_final_bill(self):

        if not self.items:

            print("\nNo items reserved.")
            return

        total = 0

        print("\n===== FINAL HOTEL FOLIO =====")

        for item in self.items:

            cost = item.calculate_item_cost()

            print(f"{item.get_name()} --> ${cost:.2f}")

            total += cost

        print("----------------------------")
        print(f"TOTAL AMOUNT: ${total:.2f}")


# ================= CREATE OBJECTS =================

room1 = Room(1, "Deluxe Room", 200, "King")
room2 = Room(2, "Single Room", 120, "Twin")

service1 = Service(3, "Spa Session", 80, 60)
service2 = Service(4, "Dinner Buffet", 50, 90)

hotel_items = [room1, room2, service1, service2]

reservation = CustomerReservation()


# ================= MAIN PROGRAM =================

while True:

    print("\n SMART HOTEL BOOKING SYSTEM ")

    print("1. View Hotel Offerings")
    print("2. Add Item To Reservation")
    print("3. View Reservation")
    print("4. Print Final Bill")
    print("5. Exit")

    try:

        choice = int(input("\nEnter your choice: "))

        # View offerings
        if choice == 1:

            print("\n===== AVAILABLE HOTEL OFFERINGS =====")

            for item in hotel_items:

                item.display_details()

                print("-------------------------")

        # Add item
        elif choice == 2:

            item_id = int(input("Enter Item ID: "))

            found = False

            for item in hotel_items:

                if item.get_id() == item_id:

                    reservation.add_item(item)

                    print(f"{item.get_name()} added successfully!")

                    found = True

                    break

            if not found:

                print("Item not found.")

        # View reservation
        elif choice == 3:

            reservation.show_reservation()

        # Final bill
        elif choice == 4:

            reservation.print_final_bill()

        # Exit
        elif choice == 5:

            print("\nThank you for using the system.")
            break

        else:

            print("Invalid menu choice.")

    except ValueError:

        print("Please enter numbers only.")