#write a python class  Bank_Account with attribute like
#customer name,ac no,balance,date of opening
#and methods like deposit,withdrawel and check baalnce

from datetime import datetime
class BankAccount:
    def set_details_from_input(self):
        self.customer_name = input("Enter customer name: ")
        self.ac_no = input("Enter account number: ")

        while True:
            try:
                self.balance = float(input("Enter initial balance: "))
                if self.balance >= 0:
                    break
                else:
                    print("Balance cannot be negative. Please enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for the balance.")

        date_of_opening = input("Enter date of opening (YYYY-MM-DD) or press Enter for today's date: ")
        if date_of_opening == "":
            self.date_of_opening = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date_of_opening = date_of_opening

    def deposit(self):
        while True:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    self.balance += amount
                    print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}")
                    break
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def withdraw(self):
        while True:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount > 0:
                    if amount <= self.balance:
                        self.balance -= amount
                        print(f"Withdrew: ${amount:.2f}. New Balance: ${self.balance:.2f}")
                        break
                    else:
                        print("Insufficient funds.")
                else:
                    print("Withdrawal amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def check_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def print_account_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.ac_no}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Date of Opening: {self.date_of_opening}")


def atm_simulation():
    account = BankAccount()
    account.set_details_from_input()

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Print Account Details")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            account.check_balance()
        elif choice == '2':
            account.deposit()
        elif choice == '3':
            account.withdraw()
        elif choice == '4':
            account.print_account_details()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

atm_simulation()

