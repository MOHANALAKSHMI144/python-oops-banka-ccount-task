from datetime import datetime

class BankAccount:
    total_accounts = 0  
    all_accounts = []  

    def init(self, account_holder, account_type, initial_balance=0):
        if not account_holder:
            raise ValueError("Account holder name cannot be empty.")
        if account_type not in ["Savings", "Current"]:
            raise ValueError("Account type must be either 'Savings' or 'Current'.")
        
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = initial_balance
        self.transactions = []  
        BankAccount.total_accounts += 1
        BankAccount.all_accounts.append(self)
        print(f"Account created for {self.account_holder} ({self.account_type}).")

    def deposit(self, amount):
        if amount <= 0 or amount > 50000:
            print("Deposit amount must be between ₹1 and ₹50,000.")
            return
        
        self.balance += amount
        self.transactions.append((datetime.now(), "Deposit", amount))
        print(f"₹{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0 or amount > 50000:
            print("Withdrawal amount must be between ₹1 and ₹50,000.")
            return
        if self.balance - amount < 0:
            print("Insufficient funds!")
            return
        
        self.balance -= amount + 10  
        self.transactions.append((datetime.now(), "Withdraw", amount))
        print(f"₹{amount} withdrawn. Transaction fee ₹10 applied. New balance: ₹{self.balance}")

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            print("Invalid target account.")
            return
        if amount <= 0 or amount > 50000:
            print("Transfer amount must be between ₹1 and ₹50,000.")
            return
        if self.balance - amount < 0:
            print("Insufficient funds!")
            return
        
        self.balance -= amount
        target_account.balance += amount
        self.transactions.append((datetime.now(), "Transfer", amount, f"To {target_account.account_holder}"))
        target_account.transactions.append((datetime.now(), "Transfer", amount, f"From {self.account_holder}"))
        print(f"₹{amount} transferred to {target_account.account_holder}. New balance: ₹{self.balance}")

    def get_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    @classmethod
    def get_total_accounts(cls):
        print(f"Total accounts in the bank: {cls.total_accounts}")

    @staticmethod
    def validate_amount(amount):
        return amount > 0 and amount <= 50000

# Example usage
acc1 = BankAccount("Alice", "Savings", 1000)
acc2 = BankAccount("Bob", "Current", 5000)

acc1.deposit(2000)
acc1.withdraw(500)
acc1.transfer(acc2, 1000)
acc1.get_transaction_history()

BankAccount.get_total_accounts()
