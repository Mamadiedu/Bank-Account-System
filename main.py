class BankAccount:
    def __init__(self, customer_name, account_number, date_of_opening, initial_balance):
        self.customer_name = customer_name
        self.account_number = account_number
        self.date_of_opening = date_of_opening
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def check_balance(self):
        print("Current Balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Current Balance:", self.balance)

# Create a bank account
account = BankAccount("Edward M", "98765", "2023-11-14", 6000)

while True:
    print("\nBank Account Operations")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Customer Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        deposit_amount = account.deposit(amount)
        print(f"Amount deposited: {deposit_amount}")
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        withdraw_amount = account.withdraw(amount)
        print(withdraw_amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        account.customer_details()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")