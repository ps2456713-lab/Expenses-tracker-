expenses = []

number = int(input("Enter number of expenses: "))


for i in range(number):

    print("\nExpense", i + 1)

    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)


# Calculate total expense

total_expense = 0

for expense in expenses:
    total_expense = total_expense + expense["amount"]


# Calculate average expense

average_expense = total_expense / len(expenses)


# Find highest expense

highest_expense = 0
highest_category = ""

for expense in expenses:

    if expense["amount"] > highest_expense:
        highest_expense = expense["amount"]
        highest_category = expense["category"]


# Category wise expense

category_expense = {}

for expense in expenses:

    category = expense["category"]
    amount = expense["amount"]

    if category in category_expense:
        category_expense[category] = category_expense[category] + amount
    else:
        category_expense[category] = amount


# Display result

print("\n================================")
print("       EXPENSE SUMMARY")
print("================================")

print("Total Expense:", total_expense)
print("Average Expense:", average_expense)

print("\nHighest Expense:")
print("Category:", highest_category)
print("Amount:", highest_expense)

print("\nCategory Wise Expense:")

for category in category_expense:
    print(category, ":", category_expense[category])
