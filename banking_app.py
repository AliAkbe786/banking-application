class Account:
    # Base class for bank accounts. Contains common attributes and methods.

    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        #Adds the specified amount to the account balance.
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        #Subtracts the specified amount from the account balance if sufficient funds exist.
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_details(self):
        #Displays the account details.
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    # Derived class for savings accounts. Adds interest calculation.
    INTEREST_RATE = 0.06  # Fixed interest rate (6%)

    def calculate_interest(self):
        # Calculates interest based on the current balance and adds it to the balance.
        interest = self.balance * self.INTEREST_RATE
        self.balance += interest
        print(f"Interest of {interest:.2f} added. New balance: {self.balance:.2f}")


# Demonstration Script
if __name__ == "__main__":
    # Create an instance of SavingsAccount with updated details
    savings_account = SavingsAccount(account_number="000415140671", account_holder="Ali Akber", balance=600000.0)

    # Display initial details
    print("Initial Account Details:")
    savings_account.display_details()

    # Perform deposit
    print("\nPerforming deposit of 200,000:")
    savings_account.deposit(200000)

    # Perform withdrawal
    print("\nPerforming withdrawal of 100,000:")
    savings_account.withdraw(100000)

    # Calculate interest
    print("\nCalculating interest:")
    savings_account.calculate_interest()

    # Final account details
    print("\nFinal Account Details:")
    savings_account.display_details()
