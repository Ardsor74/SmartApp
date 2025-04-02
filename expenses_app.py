import json

def add_expense(expenses, name, amount, category="General"):
    if category not in expenses:
        expenses[category] = {}
    expenses[category][name] = amount

def print_expenses(expenses):
    for category, items in expenses.items():
        print(f"Category: {category}")
        if isinstance(items, dict):  # Verifica se items è un dizionario
            for name, amount in items.items():
                print(f"  {name}: ${amount:.2f}")
        else:  # Gestione del caso in cui items non sia un dizionario
            print(f"  {category}: ${items:.2f}")

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
    add_expense(expenses, "Coffee", 2.50, "Food")
    add_expense(expenses, "Lunch", 10.00, "Food")
    add_expense(expenses, "Uber", 15.00, "Transport")
    print_expenses(expenses)
    save_expenses(expenses)