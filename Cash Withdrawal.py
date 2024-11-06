# Program allows user to make deposits and withdrawals from ATM

class ATM: # Created ATM Class
    def __init__(self): # Defined init method to set self initializer
        self.balance = float(input("Enter current balance: ")) # balance value is initialized after user input
        print("Current balance is $%.2f" % self.balance)

    def deposit(self): # Defined deposit function allowing user to deposit money
        amount = float(input("Enter the amount to be deposit: ")) # Asks user to enter amount to be deposited
        self.balance = self.balance + amount # Adds balance to account
        print("Deposit is successful and the balance in the account is %.2f" % self.balance)
    
    def withdraw(self): # Defined withdraw function allowing user to withdraw money
        amount = float(input("Enter the amount to withdraw: ")) # Asks user to enter amount to be withdrawn 
        if(self.balance >= amount): # Checks if balance is less than or equal to amount
            self.balance = self.balance - amount # Deducts account balance
            print("The withdrawal is successful and balance is %.2f" % self.balance)
        else:
            print("The withdrawal was unsuccessful")
            print("Please make additional deposit or withdraw an amount not greater than current balance")
            print("\n")
            option = int(input("Enter one of the option numbers: ")) # Asks user to re-enter option
            
            # Uses nested if else inside else clause
            if(option == 1):
                self.deposit()
                self.withdraw()
            else:
                (option == 2)
                self.withdraw()

amt = ATM() # Creates amt object of ATM Class

print("\n")
print("1.Deposit\n2.Withdraw") # Displays following two options to user
option = int(input("Enter one of the option numbers: ")) # Asks user select an option
print("\n")

if(option == 1):
    amt.deposit()
    amt.withdraw()
else:
    (option == 2)
    amt.withdraw()





    
