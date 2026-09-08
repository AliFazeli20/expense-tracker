# 💰 Expense Tracker

A simple and lightweight **Expense Tracker** built with Python.

This project allows users to manage their daily expenses directly from the terminal. Users can add, view, edit, and delete expenses, calculate total spending, and analyze expenses by category.

---

## ✨ Features

* ➕ Add new expenses
* 📋 View all expenses
* ✏️ Edit existing expenses
* 🗑️ Delete expenses
* 💵 Calculate total expenses
* 📂 View expenses by category
* 📊 Calculate total spending for a specific category
* 💾 Automatically save data to a JSON file
* ⚠️ Handle invalid menu selections and input errors

---

## 🛠️ Technologies

* **Python 3**
* **JSON**
* **File Handling**
* **Exception Handling**

No external libraries are required.

---

## 📁 Project Structure

```text
expense-tracker/
│
├── expense-tracker.py
├── expenses.json
├── README.md
└── .gitignore
```

### Files

| File                 | Description                    |
| -------------------- | ------------------------------ |
| `expense-tracker.py` | Main application code          |
| `expenses.json`      | Stores expense data            |
| `README.md`          | Project documentation          |
| `.gitignore`         | Specifies files ignored by Git |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AliFazeli20/expense-tracker.git
```

### 2. Navigate to the project directory

```bash
cd expense-tracker
```

### 3. Run the program

```bash
python expense-tracker.py
```

---

## 🖥️ Usage

After running the program, you will see the following menu:

```text
===== Expense Tracker =====
1. Add expense
2. Show expenses
3. Show total
4. Show by category
5. Delete expense
6. Edit expense
7. Exit

Choose an option:
```

### Example

Adding an expense:

```text
Enter expense title: Coffee
Enter amount: 80000
Enter category: Food

Expense added successfully!
```

Viewing expenses:

```text
--- Expenses ---

1. Coffee - 80000.0 - Food
2. Bus Ticket - 30000.0 - Transport
3. Book - 250000.0 - Education
```

Calculating total expenses:

```text
Total expenses: 360000.0
```

---

## 💾 Data Storage

Expenses are stored locally in a JSON file.

Example:

```json
[
    {
        "title": "Coffee",
        "amount": 80000,
        "category": "Food"
    },
    {
        "title": "Book",
        "amount": 250000,
        "category": "Education"
    }
]
```

The `expenses.json` file is automatically created when the first expense is added.

---

## 🎯 Learning Goals

This project was created to practice fundamental Python programming concepts, including:

* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* File handling
* JSON data
* Exception handling
* Basic project structure

---

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Add expense dates
* [ ] Add monthly expense reports
* [ ] Add income tracking
* [ ] Add balance calculation
* [ ] Add search functionality
* [ ] Add CSV export
* [ ] Add graphical charts
* [ ] Create a graphical user interface (GUI)
* [ ] Add a database such as SQLite

---

## 📌 Project Status

**Completed — Version 1.0**

This project is primarily intended as a learning project and can be extended with additional features over time.
