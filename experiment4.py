import datetime

email = input("Enter your email: ")

server = email.split("@")[-1]
current_datetime = datetime.datetime.now()


print(f"your email {email} is from the server {server} and the currentdate and time is {current_datetime}")

# take the user name and pancard details as input and validate the information 
name = input("Enter your name")
pan_card = input("enter the pan_card number")
if(name.isalpha()):
    print("the name is valid")
else:

    print(" the name is not valid")

if(len(pan_card)== 10 and pan_card[:5].isupper() and pan_card[5:9].isdigit() and pan_card[-1].isupper()):
    print("the pan card is valid")
else:
    print("the pan card is not valid ")

# String function examples
str = "hello world"

# capitalize
print(str.capitalize())  # Hello world

# count
print(str.count('l'))  # 3

# center
print(str.center(20, '*'))  # ****hello world*****

# startswith
print(str.startswith('he'))  # True

# find
print(str.find('world'))  # 6

# index
print(str.index('world'))  # 6

# len
print(len(str))  # 11

# rfind
print(str.rfind('l'))  # 9

# isalnum
print(str.isalnum())  # False

# isdigit
print(str.isdigit())  # False

# isalpha
print(str.isalpha())  # False

# islower
print(str.islower())  # True

# isupper
print(str.isupper())  # False

# isspace
print(str.isspace())  # False

# ljust
print(str.ljust(20, '*'))  # hello world*********

# rjust
print(str.rjust(20, '*'))  # *********hello world

# rstrip
print(str.rstrip('d'))  # hello worl

# lstrip
print(str.lstrip('h'))  # ello world

# strip
print(str.strip('h'))  # ello world

# max
print(max(str))  # w

# in
print('world' in str)  # True

# title
print(str.title())  # Hello World

# swapcase
print(str.swapcase())  # HELLO WORLD

# split
print(str.split())  # ['hello', 'world']

# enumerate
for index, char in enumerate(str):
    print(f"Index: {index}, Character: {char}")
