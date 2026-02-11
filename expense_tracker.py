import os

# Load existing expenses if file exists
expenses = []
if os.path.exists("expenses.txt"):
    with open("expenses.txt", "r") as file:
        for line in file:
            item, amount = line.strip().split(",")
            expenses.append([item, amount])
    print("Loaded previous expenses!\n")

print("My Expense Tracker")
print("Type 'done' when finished\n")

expenses = []  # This will store all expenses

while True:
    item = input("What did you spend on? ")
    
    if item == "done":
        break
    
    amount = input("How much? ")
    expenses.append([item, amount])
    print(f"Added: {amount} on {item}\n")

print("\nYour expenses:")
for expense in expenses:
    print(f"- {expense[1]} on {expense[0]}")
total = 0
for expense in expenses:
    total = total + int(expense[1])

print(f"\nTotal spent: {total}")# Save to file
with open("expenses.txt", "w") as file:
    for expense in expenses:
        file.write(f"{expense[0]},{expense[1]}\n")
print("Expenses saved!")