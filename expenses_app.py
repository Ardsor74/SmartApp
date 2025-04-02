import json

def add_expense(expenses, name, amount):
    expenses[name] = amount

def print_expenses(expenses):
    for name, amount in expenses.items():
        print(f"{name}: ${amount:.2f}")

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file)

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    expenses = load_expenses()
    add_expense(expenses, "Coffee", 2.50)
    add_expense(expenses, "Lunch", 10.00)
    print_expenses(expenses)
    save_expenses(expenses)