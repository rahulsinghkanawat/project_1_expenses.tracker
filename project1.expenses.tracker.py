# expense tacker project

# Expense Tracker Project

expenses = []  # List of all expenses in dictionary form

print("Welcome to Expense Tracker: Kharcha kam karo yaar")

while True:

    print("\n=== MENU ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = input("Please enter your choice: ")

    # 1. Add Expense
    if choice == "1":

        date = input("Kis date par kharcha hua: ")
        category = input("Kis type ka kharcha hai: ")
        description = input("Give more details: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        print("\nDone bhai! Expense added successfully.")

    # 2. View All Expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses added.")

        else:
            print("\n==== Ye raha aapka sara expenses ====")

            count = 1

            for eachkharcha in expenses:

                print(
                    f"Kharcha no {count} -> "
                    f"{eachkharcha['date']}, "
                    f"{eachkharcha['category']}, "
                    f"{eachkharcha['description']}, "
                    f"{eachkharcha['amount']}"
                )

                count = count + 1

    # 3. View Total Spending
    elif choice == "3":

        total = 0

        for eachkharcha in expenses:
            total = total + eachkharcha["amount"]

        print("\nTotal Kharcha =", total)

    # 4. Exit
    elif choice == "4":

        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice, try again.")
