import json


# -----------------------------
# Load expenses from JSON file
# -----------------------------
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# -----------------------------
# Save expenses to JSON file
# -----------------------------
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# -----------------------------
# Add a new expense
# -----------------------------
def add_expense(expenses):
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# -----------------------------
# Show all expenses
# -----------------------------
def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['title']} - "
            f"{expense['amount']} - "
            f"{expense['category']}"
        )


# -----------------------------
# Calculate total expenses
# -----------------------------
def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal expenses: {total}")


# -----------------------------
# Show expenses by category
# -----------------------------
def show_by_category(expenses):
    category = input("Enter category: ")

    total = 0
    found = False

    print(f"\n--- {category} Expenses ---")

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(
                f"{expense['title']} - "
                f"{expense['amount']}"
            )

            total += expense["amount"]
            found = True

    if found:
        print(f"Total for {category}: {total}")
    else:
        print("No expenses found in this category.")


# -----------------------------
# Delete an expense
# -----------------------------
def delete_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return

    show_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted_expense = expenses.pop(number - 1)

            save_expenses(expenses)

            print(
                f"'{deleted_expense['title']}' "
                "deleted successfully!"
            )
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# Edit an expense
# -----------------------------
def edit_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return

    show_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to edit: "))

        if 1 <= number <= len(expenses):
            expense = expenses[number - 1]

            print("\nLeave the field empty to keep the old value.")

            # Edit the expense title
            new_title = input(
                f"Enter new title ({expense['title']}): "
            )

            if new_title:
                expense["title"] = new_title

            # Edit the expense amount
            new_amount = input(
                f"Enter new amount ({expense['amount']}): "
            )

            if new_amount:
                expense["amount"] = float(new_amount)

            # Edit the expense category
            new_category = input(
                f"Enter new category ({expense['category']}): "
            )

            if new_category:
                expense["category"] = new_category

            save_expenses(expenses)

            print("Expense updated successfully!")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter valid information.")


# -----------------------------
# Main program
# -----------------------------
def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Show by category")
        print("5. Delete expense")
        print("6. Edit expense")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            show_by_category(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            edit_expense(expenses)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# -----------------------------
# Start the program
# -----------------------------
if __name__ == "__main__":
    main()