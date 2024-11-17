<img width="990" height="500" src="https://github.com/Cj-perez/PerezChristineJadeIT2104_ACPactivities/blob/main/FINALPROJECT/INTRO.png">

Table of Contents
1. [Project Overview](#project-overview)  
2. [Key Features](#key-features)  
3. [How It Works](#how-it-works)  
4. [Python Concepts and Libraries](#python-concepts-and-libraries)  
5. [Integration with SDG 12](#integration-with-sdg-12)  
6. [Setup Instructions](#setup-instructions)  
7. [Usage Instructions](#usage-instructions)  
8. [Sample Output](#sample-output)  
9. [License](#license)  
10. [Contact](#contact)

------

## Project Overview
`DineTime` is a Python-based, console-driven application designed for restaurant reservation management. Its primary objective is to provide a user-friendly interface for creating, managing, and updating reservations while ensuring efficient use of restaurant space.  

Built with `SQLite`, it features robust data handling for persistence and includes an automated table assignment system to reduce overbooking risks.

------

## Key Features
- **Interactive Menu**: Easy-to-use navigation for various functions.  
- **Reservation Management**:
  - Create, view, update, and delete reservations.  
  - Automatic assignment of available tables based on a predefined range.
- **Data Validation**: Ensures reservation times are in the future and inputs are correctly formatted.  
- **Sample Data**: Preloaded customer and reservation records for testing and demonstration.  
- **Sustainable Practices**: Aligns with global goals for responsible consumption.

------

## How It Works
1. **Database-Driven**:  
   - All reservations and customer data are stored in an SQLite database (`restaurant.db`).  
   - The database features two main tables:
     - `Customer`: Stores personal details of restaurant patrons.
     - `Reservation`: Links reservations to customer records and includes details like date, time, number of guests, and assigned table.

2. **Automated Logic**:  
   - When a new reservation is created, the program checks for available tables dynamically.  
   - Existing tables and reservations are validated to avoid clashes.

3. **OOP Implementation**:  
   - Abstract and concrete classes are used for clean code organization.  
   - Encapsulation ensures database operations are modular and reusable.

------

## Python Concepts and Libraries
### Core Python Features:
1. **Object-Oriented Programming (OOP)**:
    - **Abstraction**:  The `Person` and `ReservationBase` classes are abstract classes. They define essential attributes and methods (like `__str__ `in `Person` and `make_reservation` in `ReservationBase`) without implementation. Subclasses (`Customer` and `Reservation`) must implement these methods, allowing the abstract classes to serve as templates.
 
    - **Inheritance**: The `Customer` class inherits from the Person class. This enables `Customer` to use attributes like `name` and `email` defined in `Person`, simplifying code reuse.
    - Similarly, `Reservation` inherits from `ReservationBase`. `ReservationBase` provides a template, requiring any derived classes (like `Reservation`) to implement the `make_reservation` method.
 
    - **Polymorphism**: The `make_reservation` method in `Reservation` is an example of polymorphism. This method is defined in the abstract `ReservationBase` class, but its implementation is specific to the `Reservation` class. If another class were to inherit from `ReservationBase`, it could have its own version of `make_reservation`.

    - **Exception Handling**: Validates user input and handles incorrect formats gracefully.  

    - **Encapsulation**: The `Database` class encapsulates all database-related operations. Attributes like `self.conn` and `self.cursor` are only accessible within this class, and database actions (e.g., `create_table, get_all_reservations, delete_reservation`) are managed through class methods. This hides the complexity of database management from the rest of the program.

    - **Control Flow**:
        - The program uses structured control flow (e.g., `if, while, try-except`) to guide the user through menu options such as making, updating, viewing, and deleting reservation
        - Input validation ensures only valid data is processed.

    - **SQLite Database Integration**:
        - A relational database `(restaurant.db)` stores customer and reservation information.
     - Tables:
        - `Customer`: Stores details like name, email, and phone.
        - `Reservation`: Tracks reservation dates, times, number of guests, and table numbers.
   - SQL commands like `CREATE TABLE, INSERT, SELECT, and JOIN` are used to manage data efficiently.

    - **Modular Code**:
        - The project is divided into cohesive classes and functions:
        - `Database Class`: Encapsulates all database operations.
        - `Person and Customer Classes`: Demonstrate abstraction and inheritance.
        - `Reservation and ReservationBase Classes`: Handle reservation-related logic with polymorphism.

    - **Error Handling**:
        - Handles invalid inputs and database errors using `try-except` blocks.
        - Provides meaningful feedback for common issues (e.g., `invalid date formats or unavailable tables`).

    - **Data Handling**:
        - Implements robust input validation for fields like `dates, times, and phone numbers.`
        - Uses Python’s `datetime` module to verify and manipulate    date-time data.

    - **Optional Features**:
        - Dynamic table availability checking ensures no overbooking occurs.
        - Sample data population enables immediate testing.
        - Future-proof system with customizable table limits (easily adjustable in the code).

**Libraries**:
    - `sqlite3`: Lightweight and reliable database handling.  
    - `datetime`: Ensures reservation times are valid and in the future.  
    - `abc`: Supports abstract base classes for better code organization.  

------

## Integration with SDG 12
**DineTime** actively contributes to `Sustainable Development Goal (SDG) 12: Responsible Consumption and Production`.  
- **Minimized Waste**: Efficient table allocation prevents overbooking, saving energy and resources.  
- **Sustainable Management**: Promotes better use of restaurant space and reduces operational inefficiencies.  
- **Digital Transformation**: Reduces reliance on paper-based reservation systems.

`This project aligns technology with sustainability for meaningful impact.`

------

## Setup Instructions

**Prerequisites**
- **Python 3.7 or higher**: Download it from [python.org](https://www.python.org/downloads/).  
- **SQLite**: Pre-installed with Python, no additional installation required.  

### Installation
1. `Clone this repository`:
   git clone https://github.com/yourusername/dinetime.git
   cd dinetime
   
2. `Install dependencies (if applicable)`:
   pip install -r requirements.txt

3. `Run the program`:
   python dine_time.py

------

## Usage Instructions
1. **Start the application** and navigate using the interactive menu:
   `1.) Make a Reservation`
   `2.) View All Reservations`
   `3.) Update a Reservation`
   `4.) Delete a Reservation`
   `5.) Exit`

2. **Follow prompts** to input data for reservations, including:
   - Customer name, email, and phone number.
   - Desired date and time of the reservation.
   - Number of guests.  

3. Use options 2–4 for viewing, updating, or deleting reservations as needed.

------

## Sample Output
Here’s an example of the system in action:  

<img width="90" height="50" src="">
==================================================================
WELCOME TO DINE TIME: SMART SCHEDULING FOR RESTAURANT RESERVATIONS
==================================================================
1.) Make a Reservation
2.) View All Reservations
3.) Update a Reservation
4.) Delete a Reservation
5.) Exit

Enter your option (1-5): 1

------------------
Make a Reservation
------------------
Enter Your full name: John Doe
Enter Your email address: john.doe@example.com
Enter Your phone number: 1234567890
Enter reservation date |example: 2025-10-23| (YYYY-MM-DD): 2024-12-31
Enter reservation time  |example: 06:00PM| (HH:MMAM/PM): 07:00PM
Enter the number of guests: 4

Reservation confirmed for John Doe on 2024-12-31 at 07:00PM for 4 guests at table number 5.

------

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

------

## Contact
For any queries or contributions, reach out:  
**Email**: dine_time_support@gmail.com  
**Phone**: (043) 876-9045  
**GitHub**: 
