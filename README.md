# Interactive-Smart-Hotel-Booking-System


Video Explanation :
https://drive.google.com/file/d/1Js8FYMSv0KazYXWtNv30TxaBVG_zHf_n/view?usp=sharing


# 🏨 Smart Hotel Booking System (Terminal-Based)

## 📌 Project Description
This project is an interactive terminal-based Hotel Booking System built using Python and Object-Oriented Programming (OOP) concepts.  

It simulates a real hotel front-desk system where users can view hotel offerings, add items to a reservation, and generate a final bill with automatic service charges.

---

## ⚙️ Features

- View available hotel rooms and services
- Add items to a customer reservation using ID
- View current reservation details
- Generate final bill with automatic calculations
- Input validation and error handling (no crashes on invalid input)

---

## 🧠 OOP Concepts Implemented

### 1. Abstraction
- Created an abstract class `HotelItem`
- It defines a blueprint for all hotel items
- Contains abstract methods:
  - `calculate_item_cost()`
  - `display_details()`

---

### 2. Inheritance
- Two classes inherit from `HotelItem`:
  - `Room`
  - `Service`
- Each class has its own additional properties:
  - Room → bed size
  - Service → duration

---

### 3. Encapsulation
- Used private attributes (`__base_price`, `__item_id`, etc.)
- Data cannot be accessed or modified directly
- Controlled access using getter and setter methods with validation

---

### 4. Polymorphism
- Both `Room` and `Service` override `calculate_item_cost()`
- Each class calculates cost differently:
  - Room → adds hotel tax (15%)
  - Service → adds gratuity (20%)
- Same method name, different behavior depending on object type

---

## 🖥️ How to Run the Program

### Step 1:
Make sure you have Python installed.

### Step 2:
Open terminal in the project folder and run:

```bash
python main.py

