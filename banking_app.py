class Account:
    """Base class for a bank account"""
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self._balance = balance  # Encapsulation: using a private variable for balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def view_balance(self):
        """Displays the account balance"""
        print(f"Account Balance: ${self._balance:.2f}")


class SavingsAccount(Account):
    """Derived class for savings account with fixed interest calculation"""
    FIXED_INTEREST_RATE = 0.025  # 2.5% per annum

    def calculate_interest(self, years=1):
        """Calculates interest based on the current balance and fixed annual rate"""
        interest = self._balance * self.FIXED_INTEREST_RATE * years
        print(f"Calculated Interest for {years} year(s): ${interest:.2f}")
        return interest


# Demonstration script
if __name__ == "__main__":
    print("Savings Account Demonstration\n")

    # Create a SavingsAccount instance for Ali
    account = SavingsAccount(account_holder="Ali", account_number="SA12345", balance=1500)

    # Display initial account details
    print("Initial Account Details:")
    print(f"Account Holder: {account.account_holder}")
    print(f"Account Number: {account.account_number}")
    account.view_balance()

    # Perform transactions
    print("\nPerforming Transactions...")
    account.deposit(250)  # Deposit $250
    account.withdraw(300)  # Withdraw $300

    # Calculate interest for 1 year
    interest = account.calculate_interest(years=1)

    # Display final account details and balance
    print("\nFinal Account Details:")
    print(f"Account Holder: {account.account_holder}")
    print(f"Account Number: {account.account_number}")
    account.view_balance()
    print(f"Interest Calculated for 1 Year: ${interest:.2f}")
