""" #experimtnt 1.2

#write a program to demostrate this pattern 
""" 1
22
333
4444
5555
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="")
        print()

print_pattern(5)  # prints the pattern up to 5 rows

#WAP using a while loop only that asks the user for an number and a countdown from that number to 0
def countdown(n):
    while n >= 0:  # Include 0 in the countdown
        print(n)
        n = n - 1

# Get input from the user
num = int(input("Enter a number: "))

# Call the countdown function
countdown(num)
        #countdown(5)  # prints the countdown from 5 to 0
        #countdown(5)  # prints the countdown from 5 to 0
        

#WAP to print the reverse of the number using while loop only  
def reverse(n):
    reversed_num = 0  # Initialize a variable to store the reversed number
    while n > 0:
        remainder = n % 10  # Extract the last digit
        reversed_num = reversed_num * 10 + remainder  # Add the digit to the reversed number
        n = n // 10  # Remove the last digit from the original number

    print("Reversed number is:", reversed_num)  # Print the reversed number

# Get input from the user
num = int(input("Enter a number: "))

# Call the function to reverse the number
reverse(num) """


#WAP using for loop it should look like 
#Pass 1 - 1 2 3 4 5 
#Pass 2 - 1 2 3 4 5
#Pass 3 - 1 2 3 4 5
#Pass 4 - 1 2 3 4 5
#Pass 5 - 1 2 3 4 5
for i in range(1, 6):
    print(f"Pass {i} -", end=" ")
    for j in range(1, 6):
        print(j, end=" ")
    print()

#WAP to find the sum of series 1/1 square + 1/2 square + 1/3 square + 1/4 square + 1/n square
def sum_of_series(n):
  """Calculates the sum of the series 1/1^2 + 1/2^2 + ... + 1/n^2.

  Args:
    n: The number of terms in the series.

  Returns:
    The sum of the series.
"""   """
  total = 0
  for i in range(1, n + 1):
    total += 1 / (i ** 2)  # Calculate 1/i^2 and add it to the total
  return total

# Get input from the user
n = int(input("Enter the number of terms: "))

# Calculate and print the sum of the series
result = sum_of_series(n)
print("The sum of the series is:", result)

#WAP to print all the leap years from 1996 to 2025
def print_leap_years(start_year, end_year):
  print("Leap years between", start_year, "and", end_year, "are:")
  year = start_year
  while year <= end_year:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      break
    year += 1
  while year <= end_year:
    print(year)
    year += 4

print_leap_years(1996, 2025)



    

 """