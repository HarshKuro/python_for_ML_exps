#make a simple calculator taking multiple inputs perform calculations and make multiple function for every task and in the end use break command
#1. addition
#2. subtraction
#3. multiplication
#4. division
#5. exit
# Define functions for each mathematical operation
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculator():
    while True:
       
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

       
        choice = input("Enter your choice (1-5): ")

    
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            continue

       
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

       
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = sub(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = mul(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = div(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")

# Run the calculator
calculator()


#create a calendar 
import calendar

def display_calendar(year, month=None):
    """
    Displays a calendar for a given year and optionally a month.

    Args:
        year (int): The year for which to display the calendar.
        month (int, optional): The month for which to display the calendar. If None, displays the whole year.
    """

    if month is None:
        # Display the whole year's calendar
        print(calendar.calendar(year))
    else:
        # Display the calendar for the specified month
        print(calendar.month(year, month))

def display_calendar_interactive():
    """
    Takes year and month input from the user and displays the calendar.
    """
    try:
        year = int(input("Enter the year: "))
        month_input = input("Enter the month (1-12, or press Enter for the whole year): ")

        if month_input:
            month = int(month_input)
            if 1 <= month <= 12:
                display_calendar(year, month)
            else:
                print("Invalid month. Please enter a number between 1 and 12.")
        else:
            display_calendar(year)

    except ValueError:
        print("Invalid input. Please enter valid integer values for year and month.")

if __name__ == "__main__":
    display_calendar_interactive()