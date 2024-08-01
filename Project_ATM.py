class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = None
        self.transaction_history = []

    def set_pin(self):
        new_pin = input("Set your 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print("PIN set successfully!")
        else:
            print("Invalid PIN format. Please enter a 4-digit PIN.")

    def verify_pin(self):
        if self.pin is None:
            print("No PIN set. Please set a PIN first.")
            return False
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN. Try again.")
            return False

    def withdraw(self):
        if self.verify_pin():
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew: ₹{amount}")
                print(f"₹{amount} withdrawn successfully!")
            else:
                print("Insufficient balance.")

    def deposit(self):
        if self.verify_pin():
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            self.transaction_history.append(f"Deposited: ₹{amount}")
            print(f"₹{amount} deposited successfully!")

    def balance_inquiry(self):
        if self.verify_pin():
            print(f"Your current balance is: ₹{self.balance}")

    def view_transaction_history(self):
        if self.verify_pin():
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
            if not self.transaction_history:
                print("No transactions yet.")

    def change_pin(self):
        if self.verify_pin():
            new_pin = input("Enter your new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN changed successfully!")
            else:
                print("Invalid PIN format. Please enter a 4-digit PIN.")

    def start(self):
        while True:
            print("\nATM Machine")
            print("1. Set PIN")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Balance Inquiry")
            print("5. View Transaction History")
            print("6. Change PIN")
            print("7. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.set_pin()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.balance_inquiry()
            elif choice == '5':
                self.view_transaction_history()
            elif choice == '6':
                self.change_pin()
            elif choice == '7':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Create ATM object and start the ATM
atm = ATM()
atm.start()