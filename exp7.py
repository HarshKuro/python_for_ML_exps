""" #bank account class encapsulation in python . create a bank account class that uses encapsulation that manages attributes like balance . method to withdraw money , to show current balacnce, to get balance.
class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    try:
        account = BankAccount(1000)

        account.show_balance()
        print(f"Initial Get balance: {account.get_balance()}")

        account.deposit(500)
        account.show_balance()
        print(f"Get balance after deposit: {account.get_balance()}")

        account.withdraw(200)
        account.show_balance()
        print(f"Get balance after withdrawal: {account.get_balance()}")
        account.deposit(250.50)
        account.show_balance()
        print(f"Get balance after float deposit: {account.get_balance()}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")



#show the concept of method overloading in python create a parent constructor and a child method that overloads the parent method.
# Demonstrating method overloading using JoJo characters.

class Joestar:
    def __init__(self, name="Jonathan Joestar", stand=None):
        self.name = name
        self.stand = stand

    def show_details(self):
        print(f"Name: {self.name}")
        if self.stand:
            print(f"Stand: {self.stand}")
        else:
            print("Stand: None")

class Jotaro(Joestar):
    def __init__(self, name="Jotaro Kujo", stand="Star Platinum", catchphrase="Yare Yare Daze"):
        # Overloading the parent constructor by adding a catchphrase parameter
        super().__init__(name, stand)
        self.catchphrase = catchphrase

    def show_details(self):
        # Overriding the parent method to include the catchphrase
        super().show_details()
        print(f"Catchphrase: {self.catchphrase}")

if __name__ == "__main__":
    # Parent class instance
    jonathan = Joestar()
    jonathan.show_details()

    print("\n")

    # Child class instance
    jotaro = Jotaro()
    jotaro.show_details()
 """

#show the concept of method overriding in python create a parent constructor and a child method that overrides the parent method.
class parent:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Parent class show method")
class child(parent):
    def show(self):
        print("Child class show method")
#creating object of child class
c=child("child")
c.show()


# Demonstrating method overloading using JoJo characters from Parts 1 to 9.

""" class Joestar:
    def __init__(self, name="Unknown Joestar", stand=None):
        self.name = name
        self.stand = stand

    def show_details(self):
        print(f"Name: {self.name}")
        if self.stand:
            print(f"Stand: {self.stand}")
        else:
            print("Stand: None")


class Jonathan(Joestar):
    def __init__(self):
        super().__init__(name="Jonathan Joestar", stand=None)

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"I will defeat you, Dio!\"")


class Joseph(Joestar):
    def __init__(self):
        super().__init__(name="Joseph Joestar", stand="Hermit Purple")

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"Your next line is...\"")


class Jotaro(Joestar):
    def __init__(self):
        super().__init__(name="Jotaro Kujo", stand="Star Platinum")

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"Yare Yare Daze.\"")


class Josuke(Joestar):
    def __init__(self):
        super().__init__(name="Josuke Higashikata", stand="Crazy Diamond")

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"Don't insult my hair!\"")


class Giorno(Joestar):
    def __init__(self):
        super().__init__(name="Giorno Giovanna", stand="Gold Experience")

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"I, Giorno Giovanna, have a dream!\"")


class Jolyne(Joestar):
    def __init__(self):
        super().__init__(name="Jolyne Cujoh", stand="Stone Free")

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"Yare Yare Dawa.\"")


class Johnny(Joestar):
    def __init__(self):
        super().__init__(name="Johnny Joestar", stand="Tusk")

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"Spin to win!\"")


class Gappy(Joestar):
    def __init__(self):
        super().__init__(name="Josuke Higashikata (Gappy)", stand="Soft & Wet")

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"I can take something from you.\"")


class Jodio(Joestar):
    def __init__(self):
        super().__init__(name="Jodio Joestar", stand="November Rain")

    def show_details(self):
        super().show_details()
        print("Catchphrase: \"This is the mechanism for becoming filthy rich.\"")


if __name__ == "__main__":
    # Create instances of each JoJo and display their details
    jojos = [
        Jonathan(),
        Joseph(),
        Jotaro(),
        Josuke(),
        Giorno(),
        Jolyne(),
        Johnny(),
        Gappy(),
        Jodio()
    ]

    for jojo in jojos:
        jojo.show_details()
        print("\n") """

# --- BankAccount Class demonstrating Encapsulation ---

class BankAccount:
    """
    Represents a bank account with encapsulated balance.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes the bank account.
        Ensures the initial balance is not negative.
        """
        # Encapsulated attribute: _balance is intended for internal use.
        if initial_balance >= 0:
            self._balance = initial_balance
        else:
            print("Initial balance cannot be negative. Setting balance to 0.")
            self._balance = 0

    def deposit(self, amount):
        """
        Deposits a positive amount into the account.
        """
        # Method to modify the private balance safely
        if amount > 0:
            self._balance += amount
            print(f"Successfully deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a positive amount from the account if funds are sufficient.
        """
        # Method controls withdrawal logic, checking funds
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            print(f"Successfully withdrew: ${amount:.2f}")

    def get_balance(self):
        """
        Returns the current account balance.
        Provides controlled read access to the balance.
        """
        # Getter method to safely access the balance
        return self._balance

    def show_balance(self):
        """
        Displays the current account balance to the user.
        """
        # User-friendly method to display the balance
        print(f"Current balance: ${self._balance:.2f}")

# --- Example Usage ---
# Create an account
my_account = BankAccount(1000)

# Show initial balance
my_account.show_balance() # Output: Current balance: $1000.00

# Deposit money
my_account.deposit(500)   # Output: Successfully deposited: $500.00
my_account.show_balance() # Output: Current balance: $1500.00

# Withdraw money
my_account.withdraw(200)  # Output: Successfully withdrew: $200.00
my_account.show_balance() # Output: Current balance: $1300.00

# Attempt invalid withdrawal
my_account.withdraw(2000) # Output: Insufficient funds.
my_account.withdraw(-50)  # Output: Withdrawal amount must be positive.

# Get balance using the getter method
current_bal = my_account.get_balance()
print(f"Balance retrieved via get_balance(): ${current_bal:.2f}") # Output: Balance retrieved via get_balance(): $1300.00

# Attempt direct access (discouraged due to the underscore convention)
# print(my_account._balance) # Works, but violates the convention of encapsulation