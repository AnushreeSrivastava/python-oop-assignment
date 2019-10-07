# Author : Anushree Srivastava
# Student ID: 801084977
# ITCS 6112 - Assignment: Programming - 1
# Question 2


class BankAccount:
    """
    Contructor for class Bank Account to initialize Account Number, Account Type,Current account balance,
    Account holders
    """

    acct_types = ["Saving", "Checking"]

    def __init__(
        self,
        acct_number,
        acct_type,
        curr_balance,
        acct_holder=None,
        allowed_types=acct_types,
    ):
        self.acct_number = acct_number
        self.acct_holder = acct_holder if acct_holder is not None else []
        if acct_type not in allowed_types:
            raise ValueError("%s is not a valid Account type." % acct_type)
        self.acct_type = acct_type
        self.curr_balance = curr_balance

    def get_account_number(self):
        """
        Function to retrieve Account Number
        :return: acct_number
        """
        return self.acct_number

    def get_account_type(self):
        """
        Function to retrieve Account Type
        :return: acct_type
         """
        return self.acct_type

    def get_account_holders(self):
        """
        Function to retrieve Account Type
        :return: acct_type
        """
        return self.acct_holder

    def get_current_balance(self):
        """
        Function to retrieve Account Current Balance
        :return: curr_balance
        """
        return self.curr_balance

    def deposit(self, amt):
        """
        Function to deposit given amount of money to the account
        """
        self.curr_balance = self.get_current_balance() + amt

    def withdraw(self, amt):
        """
        Function to withdraw given amount of money from the account
        """
        if self.curr_balance >= amt:
            self.curr_balance = self.get_current_balance() - amt
        else:
            print("Insufficient balance! Amount Can not be withdrawn.")

    def add_account_holder(self, name):
        """
        Function to add Account Holders
        """
        self.acct_holder.append(name)


def print_account_details(account):
    """
    function to print all the Account Details
    :param account:
    :return:
    """
    print("The Account Number is: ", account.get_account_number())
    print("The Account Type is: ", account.get_account_type())
    print("The Account Holder(s) is/are: ", account.get_account_holders())
    print("The Account Current Balance is: ", account.get_current_balance())


def main():
    """
    i.Create a Checking account with account number 12345678 with an initial deposit of $1000
    for the account holder Gregory House
    :return:
    """
    account1 = BankAccount(12345678, "Checking", 1000, ["Gregory House"])

    """
    ii.	Display the current state of House’s account
    """
    print_account_details(account1)

    """
    House won $100 which is deposited into the account and the updated balance is shown
    """
    print("\nHouse just won a $100 bet against his colleague James Wilson!!")
    account1.deposit(100)
    print("The Updated Balance is:", account1.get_current_balance())

    """
    The repair costs $2500, since House does not have sufficient balance therefore a message is displayed
    and nothing gets deducted from the account
    """
    print("\nThe ceiling in House’s bathroom fell through and the repair costs $2500")
    account1.withdraw(2500)
    print("The Updated Balance is:", account1.get_current_balance())


main()
