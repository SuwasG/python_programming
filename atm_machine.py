class Account:
    __min_balance=1000
    def __init__(self, acc_no, pin, balance=0):
        self.__acc_no  = acc_no
        self.__pin=pin 
        self.__balance=balance 

    def display_balance(self):
        print(f"The balance available is: {self.__balance}")
    
    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            print(f"{amount} deposited. New balance is {self.__balance}")
        else:
            print("Invalid amount for deposit.")
    
    def withdraw(self, amount):
        if amount>0:

            if self.__balance - amount>=self.__min_balance:
                self.__balance-=amount 
                print(f"{amount} withdrawn. New balance is: {self.__balance}")
            else:
                print("Insufficient balance. You can not withdraw that amount.")
        else:
            print("Invalid amount for withdrawl.")

class ATM:
    def __init__(self):
        # initializes empty dictionary named 'accounts' used to store mapping between the acc_no and their corresponding 'Account' objects.
        self.__accounts={} # stores acc_no: Account mapping
    
    def create_account(self, acc_no, pin, initial_balance=0):
        if acc_no not in self.__accounts:
            new_account=Account(acc_no, pin, initial_balance)
            self.__accounts[acc_no]=new_account # adds the new entry to the 'accounts' dictionary
            print('Account created successfully!')
        else:
            print("Account Already Exists. Proceed to continue.")
    
    def authenticate(self, acc_no, pin):
        if acc_no in self.__accounts:
            '''
            In Python, private attributes can still be accessed from outside the class, but their names are mangled to make them harder to access accidentally.

            In this case, __pin is a private attribute of the Account class. When accessing it from outside the class, you need to use the mangled name, which is _Account__pin.

            So, self.__accounts[acc_no]._Account__pin correctly accesses the private __pin attribute of the Account object stored in the __accounts dictionary.
            '''
            if self.__accounts[acc_no]._Account__pin==pin: # mangled name
                # retrives tha 'Account' objects associated with the given acc_no from 'accounts' dictionary using the acc_no as the key. It then checks if the 'pin' attribute of the 'Account' object matches the providesd 'pin'.
                return True 
            else:
                print("Incorrect Pin.")
        else:
            print("Account Does Not Exist")

    def check_balance(self, acc_no):
        if self.authenticate(acc_no, self.__accounts[acc_no]._Account__pin):
            self.__accounts[acc_no].display_balance()
    
    def deposit(self, acc_no, amount):
        if self.authenticate(acc_no, self.__accounts[acc_no]._Account__pin):
            self.__accounts[acc_no].deposit(amount)
    
    def withdraw(self, acc_no, amount):
        if self.authenticate(acc_no, self.__accounts[acc_no]._Account__pin):
            self.__accounts[acc_no].withdraw(amount)

atm1=ATM()

# create accounts
atm1.create_account("111111", "1111", 1500)
atm1.create_account("222222", "2222", 500)

# check balance
atm1.check_balance("111111")
atm1.deposit("111111", 4000)
atm1.withdraw("111111", 500)
atm1.check_balance("111111")

atm1.create_account("111111", "2222", 3333)