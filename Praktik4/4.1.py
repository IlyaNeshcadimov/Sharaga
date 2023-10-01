class BankAccount:
    """ An abstract base class representing a bank account. """
    
    currency = '$'
    
    def __init__(self, customer, account_number, balance=0):
        """
        Initialize the BankAccount class with a customer, account number,
        and opening balance (which defaults to 0.)
        """
        if not self.validate_account_number(account_number):
            raise ValueError('Invalid account number')
        
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    @staticmethod
    def validate_account_number(account_number):
        """
        Validate the account number using the Luhn algorithm.
        """
        account_number = str(account_number)
        account_number = account_number[::-1]
        total = 0
        
        for i, digit in enumerate(account_number):
            digit = int(digit)
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit
        
        return total % 10 == 0

    def deposit(self, amount):
        """ Deposit amount into the bank account. """
        if amount > 0:
            self.balance += amount
        else:
            print('Invalid deposit amount:', amount)

    def withdraw(self, amount):
        """
        Withdraw amount from the bank account, ensuring there are sufficient
        funds.
        """
        if amount > 0:
            if amount > self.balance:
                print('Insufficient funds')
            else:
                self.balance -= amount
        else:
            print('Invalid withdrawal amount:', amount)

class CurrentAccount(BankAccount):
    def __init__(self, customer, account_number, balance=0, overdraft_limit=0):
        super().__init__(customer, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.balance + self.overdraft_limit:
                print('Insufficient funds')
            else:
                self.balance -= amount
        else:
            print('Invalid withdrawal amount:', amount)
