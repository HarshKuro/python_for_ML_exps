""" 
program to illustrate the use of conditional (if else) and iteration statements
# Conditional Statements (if-else)
age = int(input("Enter your age: "))
if age >= 18:
  print("You are eligible to vote.")  # Code block executed if the condition is True
else:
  print("You are not eligible to vote yet.")  # Code block executed if the condition is False
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)


# Iteration Statements (while loop)
count = 1
while count <= 1000:
  print(count)
  count += 1  
 """
  #WAP to determine the charachetr enetred by the user if its is a digit (is alpha is digit) something like that if you are writing alphabet it ll print the alpha if you enter digit it ll print digit it will be give output digit

""" for i in range(2):
  char = input("Enter a character: ")
  if char.isalpha():
    print("Alphabet")
  elif char.isdigit():
    print("Digit")
  else:
    print("Special Character") """

    #WAP to enter any charchetr if the nenter3ed character is n lower case then convert it into upper case.. and if it is in a uppeer case then convert it into lower case 

char = input("Enter a character: ")
if char.islower():
  print(char.upper())
elif char.isupper():
 print(char.lower())
else:
 print("Invalid input")

 #program to test whether the number enterted by the user is negative positive or equal to zero for this make the use of if,elif,and else 

char = int(input("Enter a number: "))
if char > 0:
 print("Positive number")
elif char < 0:
 print("Negative number")
else:
 print("Zero")  

#create a list show that the list is ordered and mutebale 
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
fruits[0] = "grape"
print(fruits)  # Output: ['grape', 'banana', 'cherry']
fruits.sort()
print(fruits)  # Output: ['banana', 'cherry', 'grape']


