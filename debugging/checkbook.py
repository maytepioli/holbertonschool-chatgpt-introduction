class Checkbook:
    """
    A simple checkbook class to manage bank transactions such as deposits and withdrawals.

    Attributes:
    balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes a new Checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Description:
        This method adds the given amount to the current balance and prints
        a confirmation message along with the updated balance.

        Parameters:
        amount (float): The amount of money to deposit into the checkbook.

        Returns:
        None
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if sufficient funds are available.

        Description:
        This method subtracts the given amount from the current balance if
        there are enough funds. It prints a confirmation message or an error message
        if there are insufficient funds.

        Parameters:
        amount (float): The amount of money to withdraw from the checkbook.

        Returns:
        None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance in the checkbook.

        Description:
        This method prints the current balance to the console.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class via user input.

    Description:
    This function creates an instance of the Checkbook class and repeatedly
    prompts the user to perform various actions such as depositing, withdrawing,
    checking the balance, or exiting the program. It handles user input and
    invokes the appropriate methods on the Checkbook instance.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
