import sqlite3
from datetime import datetime
from abc import ABC, abstractmethod

# Handles all database-related tasks
class Database:# Initialize the database connection
    def __init__(self, DineTime='restaurant.db'):
        self.DineTime = DineTime # Save the database file name
        self.conn = sqlite3.connect(self.DineTime)# Establish the connection
        self.cursor = self.conn.cursor() #  Get a cursor for executing SQL commands

    def get_reservation(self, reservation_id):# Getting the single reservation based on its ID
        """Fetch a single reservation by reservation_id."""
        self.cursor.execute('''
            SELECT reservation_id, customer_id, reservation_date, reservation_time, num_guests, table_number
            FROM Reservation
            WHERE reservation_id = ?
        ''', (reservation_id,))
        return self.cursor.fetchone()

    # Database, create the necessary tables if they don't already exist
    def create_table(self):
       
        # Drop the tables if they exist (for development purposes) when it exit the terminal
        self.cursor.execute('DROP TABLE IF EXISTS Customer')
        self.cursor.execute('DROP TABLE IF EXISTS Reservation')
        
        # Create the Customer table
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Customer (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                phone VARCHAR(15)
            )
        ''')
        
        # Create the Reservation table
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Reservation (
                reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                reservation_date TEXT NOT NULL,
                reservation_time TEXT NOT NULL,
                num_guests INTEGER NOT NULL,
                table_number INTEGER NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE
            )
        ''')
        
        # Save the changes to the database
        self.conn.commit()

    # Database, Populates the database with sample customer and reservation data
    def populate_sample_data(self):
        self.cursor.execute("INSERT INTO Customer (name, email, phone) VALUES ('Kathryn Chandria Manuel Bernardo', 'Kath@gmail.com', '09123454367')")
        self.cursor.execute("INSERT INTO Customer (name, email, phone) VALUES ('Beanca Marie Landero Binene', 'Bea@gmail.com', '09235432876')")
        self.cursor.execute("INSERT INTO Customer (name, email, phone) VALUES ('Kirsten Danielle Tan Delavin', 'Kisses@gmail.com', '09237654753')")
        self.cursor.execute(''' 
            INSERT INTO Reservation (customer_id, reservation_date, reservation_time, num_guests, table_number)
            VALUES (1, '2024-12-25', '07:00PM', 4, 1)
        ''')
        self.cursor.execute(''' 
            INSERT INTO Reservation (customer_id, reservation_date, reservation_time, num_guests, table_number)
            VALUES (2, '2024-12-26', '12:00PM', 2, 2)
        ''')
        self.cursor.execute(''' 
            INSERT INTO Reservation (customer_id, reservation_date, reservation_time, num_guests, table_number)
            VALUES (3, '2024-12-27', '10:00PM', 3, 3)
        ''')
        self.conn.commit()

    # Getting all reservations in the database
    def get_all_reservations(self):
        self.cursor.execute(''' 
            SELECT r.reservation_id, c.name, c.email, c.phone, r.reservation_date, r.reservation_time, r.num_guests, r.table_number
            FROM Reservation r
            JOIN Customer c ON r.customer_id = c.customer_id
        ''')
        return self.cursor.fetchall()

        # Updating the reservation in the system
    def update_reservation(self, reservation_id, reservation_date, reservation_time, num_guests):
        self.cursor.execute(''' 
            UPDATE Reservation 
            SET reservation_date = ?, reservation_time = ?, num_guests = ? 
            WHERE reservation_id = ?
        ''', (reservation_date, reservation_time, num_guests, reservation_id))
        self.conn.commit()
        print("-"*44)
        print(f"Reservation with ID {reservation_id} updated successfully.")
        print("-"*44)


    # Deletes the single reservation by its ID
    def delete_reservation(self, reservation_id):
        try:
            reservation_id = int(reservation_id)  # Ensure it's an integer
            self.cursor.execute('SELECT * FROM Reservation WHERE reservation_id = ?', (reservation_id,))
            reservation = self.cursor.fetchone()
            
            if reservation:
                self.cursor.execute('DELETE FROM Reservation WHERE reservation_id = ?', (reservation_id,))
                self.conn.commit()
                print("-"*44)
                print(f"Reservation with ID {reservation_id} deleted successfully.")
                print("-"*44)
            else:
                print("ID not found. Please enter a valid reservation ID.")
        except ValueError:
            print("Invalid ID format. Please enter a valid numeric reservation ID.")

    # Retrieves the next available table number & available 20 tables
    def get_available_table_number(self):
        self.cursor.execute('SELECT table_number FROM Reservation')
        occupied_tables = {row[0] for row in self.cursor.fetchall()}
        for table_num in range(1, 21):
            if table_num not in occupied_tables:
                return table_num
        return None

    # Close the database connection
    def close(self):
        self.conn.close()


# Abstract base class for Person (Abstraction & Encapsulation)
class Person(ABC):  # Abstraction, Person class defines abstract methods for its subclasses to implement
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def __str__(self):# Abstract method, Must be implemented by subclasses
        pass

# Child class, Customer (Inheritance)
class Customer(Person): # Inheritance, Customer inherits from Person
    def __init__(self, name, email, phone):
        super().__init__(name, email)   # Calls the constructor of the parent (Person) class
        self.phone = phone

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"

# Abstract base class for Reservation (Abstraction)
class ReservationBase(ABC): # Abstraction: ReservationBase class defines an abstract method
    @abstractmethod
    def make_reservation(self, db):  # Abstract method to be implemented by subclass
        pass

# Child class, Reservation (Inheritance)
class Reservation(ReservationBase): # Inheritance, Reservation inherits from ReservationBase
    def __init__(self, customer, reservation_date, reservation_time, num_guests):
        self.customer = customer
        self.reservation_date = reservation_date
        self.reservation_time = reservation_time
        self.num_guests = num_guests

    def make_reservation(self, db): # Polymorphism, Overriding make_reservation from ReservationBase
        table_number = db.get_available_table_number() # Using encapsulated method from Database class
        if table_number is None:
            print("-"*44)
            print("Error: Reservation limit reached. No more tables are available.")
            print("-"*44)
            return False

        try:
            res_date = datetime.strptime(self.reservation_date, '%Y-%m-%d')# for date
            res_time = datetime.strptime(self.reservation_time, '%I:%M%p')# for time
            res_datetime = datetime.combine(res_date, res_time.time())
            if res_datetime < datetime.now():
                print("-"*44)
                print("Error: Reservation time must be in the future.")
                print("-"*44)
                return False
        except ValueError:
            print("-"*90)
            print("Error: Invalid date/time format. Use 'YYYY-MM-DD' for date and 'HH:MM AM/PM' for time.")
            print("-"*90)
            return False

        # Database, Insert data Customer
        db.cursor.execute(''' 
            INSERT INTO Customer (name, email, phone) VALUES (?, ?, ?)
        ''', (self.customer.name, self.customer.email, self.customer.phone))
        customer_id = db.cursor.lastrowid

        # Database, Insert data Reservation
        db.cursor.execute(''' 
            INSERT INTO Reservation (customer_id, reservation_date, reservation_time, num_guests, table_number)
            VALUES (?, ?, ?, ?, ?)
        ''', (customer_id, self.reservation_date, self.reservation_time, self.num_guests, table_number))
        db.conn.commit()

        print("-" * 130)
        print(f"Reservation confirmed for {self.customer.name} on {self.reservation_date} at {self.reservation_time} for {self.num_guests} guests at table number {table_number}.")
        print("-" * 130)
        return True


# Main function for user interaction
def main():
    db = Database()
    db.create_table()
    db.populate_sample_data()

        # Welcome & Information & Main Menu
    while True:
        print("\n" + "\t\t" + "="*66)
        print("\t\tWELCOME TO DINE TIME: SMART SCHEDULING FOR RESTAURANT RESERVATIONS")
        print("\t\t" + "="*66)

        print("-"*95)
        print("\tWelcome to DineTime: Smart Scheduling for Restaurant Reservations! We're excited \nto provide you with a seamless and enjoyable reservation experience. Thank you for choosing us, \nand we look forward to serving you!.")
        print("-"*95)

        print("\n" + "\t\t\t\t" + "="*26)
        print("\t\t\t\t\tINFORMATION")
        print("\t\t\t\t" + "="*26)
        print("-"*95)
        print("\tPhone:(043) 876-9045 \t\t\tEmail:DineTime@Gmail.com \n\tLocation: Alangilan,Golden Country \tOpen Hours: Mon-Sun, 24/7")
        print("-"*95)

        print("\n" + "\t\t\t\t" + "="*30)
        print("\t\t\t\tRestaurant Reservation System")
        print("\t\t\t\t" + "="*30)
        print("\t\t\t\t1.) Make a Reservation")
        print("\t\t\t\t2.) View All Reservations")
        print("\t\t\t\t3.) Update a Reservation")
        print("\t\t\t\t4.) Delete a Reservation")
        print("\t\t\t\t5.) Exit")
        print("\t\t\t\t" + "="*30)

        option = input("\t\t\t\tEnter your option (1-5): ")

            # Option 1(Making a Reservation)
        if option == "1":
            print("\n" + "\t\t\t\t" + "-"*30)
            print("\t\t\t\tMake a Reservation")
            print("\t\t\t\t" + "-"*30)
            name = input("\t\t\t\tEnter Your full name: ")
            email = input("\t\t\t\tEnter Your email address: ")
            phone = int(input("\t\t\t\tEnter Your phone number: "))
            reservation_date = input("\t\t\t\tEnter reservation date |example: 2025-10-23| \n\t\t\t\t(YYYY-MM-DD): ")
            reservation_time = input("\t\t\t\tEnter reservation time |example: 06:00PM| \n\t\t\t\t(HH:MMAM/PM): ")
            num_guests = int(input("\t\t\t\tEnter the number of guests: "))

            customer = Customer(name, email, phone)
            reservation = Reservation(customer, reservation_date, reservation_time, num_guests)
            reservation.make_reservation(db)

            # Pop up when done executing each option then "press 6" to return to main menu
            back_to_main = int(input("\nPress 6 to go back to the main menu: "))
            if back_to_main == '6':
                continue  # This ensures the loop goes back to the main menu

                # Option 2(Viewing all Reservation)
        elif option == "2":
            print("\n" + "\t\t\t\t" + "-"*30)
            print("\t\t\t\tView All Reservations")
            print("\t\t\t\t" + "-"*30)
            reservations = db.get_all_reservations()
            for res in reservations:
                print(f"Reservation ID: {res[0]} | Name: {res[1]} | Email: {res[2]} | Date: {res[4]} | Time: {res[5]} | Guests: {res[6]} | Table: {res[7]}")

            # Pop up when done executing each option then "press 6" to return to main menu
            back_to_main = int(input("\nPress 6 to go back to the main menu: "))
            if back_to_main == '6':
                continue  # This ensures the loop goes back to the main menu

                # Option 3(Updating Reservation)
        elif option == '3':
            print("\n" + "\t\t\t\t" +"-"*30)
            print("\t\t\t\tUpdate Reservation")
            print("\t\t\t\t" +"-"*30)
            reservation_id = int(input("\t\t\t\tEnter the reservation ID to update: "))
            reservation = db.get_reservation(reservation_id)
            if reservation:
                print(f"\t\t\t\tCurrent reservation: Date: {reservation[2]}, Time: {reservation[3]}, Guests: {reservation[4]}")
                reservation_date = input("\t\t\t\tEnter new reservation date |example: 2025-10-23| \n\t\t\t\t(YYYY-MM-DD): ")
                reservation_time = input("\t\t\t\tEnter new reservation time |example: 06:00PM| \n\t\t\t\t(HH:MMAM/PM): ")
                num_guests = int(input("\t\t\t\tEnter new number of guests: "))
                db.update_reservation(reservation_id, reservation_date, reservation_time, num_guests)
            else:
                print("Reservation ID not found.")

            # Pop up when done executing each option then "press 6" to return to main menu
            back_to_main = int(input("\nPress 6 to go back to the main menu: "))
            if back_to_main == '6':
                continue  # This ensures the loop goes back to the main menu

                # Option 4(Deleting Reservation)
        elif option == "4":
            print("\n" + "\t\t\t\t" + "-"*30)
            print("\t\t\t\tDelete a Reservation")
            print("\t\t\t\t" + "-"*30)
            reservation_id = int(input("\t\t\t\tEnter the reservation ID to delete: "))
            db.delete_reservation(reservation_id)

            # Pop up when done executing each option then "press 6" to return to main menu
            back_to_main = int(input("\nPress 6 to go back to the main menu: "))
            if back_to_main == '6':
                continue  # This ensures the loop goes back to the main menu

                # Option 5(Exiting the system)
        elif option == '5':
                print("\n" + "\t\t\t\t" "Exiting system...")
                print("\n" + "\t\t" + "="*53)
                print("\t\tTHANK YOU FOR MAKING A RESERVATION HERE IN DINETIME!")
                print("\t\t" +"="*53)
                db.close()
                break
        else:
            print("Invalid choice. Please try again.")

            # Pop up when done executing each option then "press 6" to return to main menu
            back_to_main = int(input("\nPress 6 to go back to the main menu: "))
            if back_to_main == '6':
                continue  # This ensures the loop goes back to the main menu

if __name__ == "__main__":
    main()