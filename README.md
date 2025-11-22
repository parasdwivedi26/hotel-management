# Hotel Management System (Python)

A console-based Hotel Management System developed in Python. It enables users to book rooms, calculate rent, order food, generate restaurant bills, and produce a final combined bill. The system follows an Object-Oriented Programming (OOP) approach using four main classes: **Customer**, **Room**, **Restaurant**, and **TotalBill**.

---

## 📌 Features

### 🧑‍💼 Customer Module

* Takes customer name and address
* Validates room number input
* Prevents invalid entries (negative or non-numeric)

### 🏨 Room Management

* Four room types:

  * AC Large – ₹10,000/day
  * AC Small – ₹8,000/day
  * Non-AC Large – ₹4,000/day
  * Non-AC Small – ₹3,000/day
* Validates room type selection (1–4)
* Calculates rent based on number of days

### 🍽 Restaurant Module

* Menu includes:

  * Water
  * Tea
  * Breakfast Combo
  * Lunch
  * Dinner
* Supports multiple food orders with quantity
* Validates inputs
* Calculates total food bill

### 🧾 Billing System

* Combines:

  * Room Rent
  * Food Bill
  * Extra Charges (₹500 service charge)
* Shows detailed receipt
* Computes final payable amount

### 📋 Additional Features

* Displays list of booked rooms
* Prevents double room booking
* Full input validation for all numeric fields

---

## 📁 Project Structure

```
Hotel_Management_System/
│
├── Hotel ma.py          → Main project file
├── README.md            → Project documentation
└── Report.pdf           → Full project report (optional)
```

---

## ▶️ How to Run

1. Install **Python 3**.
2. Save the file as:

```
hotel.py
```

3. Open terminal/cmd in the file directory.
4. Run:

```
python hotel.py
```

---

## 🧱 Classes Used

### **Customer**

Handles:

* Customer name
* Address
* Room number validation

### **Room**

Handles:

* Room type selection
* Days of stay
* Rent calculation

### **Restaurant**

Handles:

* Menu display
* Ordering food
* Food bill calculation

### **TotalBill**

* Inherits from all three modules
* Applies extra charges
* Generates final bill

---

## 🧪 Testing Performed

* Checked invalid room numbers
* Verified invalid room types
* Tested incorrect food choices & quantities
* Ensured double booking prevention
* Validated bill computations

---

## 🚀 Future Enhancements

* Integrate database (SQLite/MySQL)
* Add login system
* Build GUI (Tkinter/PyQt)
* Develop a web version (Flask/Django)
* Export receipts as PDF

---

## 👨‍💻 Author

PARAS DWIVEDI