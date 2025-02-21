#wAP that uses a list to store the numbers guessed by the player. the player needs to guess a number and the program will tell wether the guess is correct or not. the program should also store all previous guesses in a list. if the number is very low print number is very low,or high or correct using random library all the wrong guesses need to be store in a list. 

#task 2 . use all the fuctions that we have discussed in our previous lectures


""" import random

def guessing_game():
    secret_number = random.randint(1, 100)
    guesses = []  # List to store all guesses
    wrong_guesses = [] # List to store wrong guesses

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses.append(guess)  # Add the guess to the list

            if guess < secret_number:
                if secret_number - guess > 20: #if difference is more than 20, very low
                  print("Your guess is very low.")
                else:
                    print("Your guess is low.")
                wrong_guesses.append(guess)
            elif guess > secret_number:
                if guess - secret_number > 20: #if difference is more than 20, very high
                  print("Your guess is very high.")
                else:
                  print("Your guess is high.")
                wrong_guesses.append(guess)
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print("Your guesses:", guesses)
                print("Wrong guesses:", wrong_guesses)
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    guessing_game() """




import random 
def guessing_game():
    secret_number = random.randint(1, 100)
    guesses = []  
    wrong_guesses = []
    print ("welcome to the guess game")
    print ("think a number between 1 to 100")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses.append(guess)

            if guess < secret_number:
                if secret_number - guess > 20:
                  print("Your guess is very low.")
                else:
                    print("Your guess is low.")
                wrong_guesses.append(guess)
            elif guess > secret_number:
                if guess - secret_number > 20:
                  print("Your guess is very high.")
                else:
                  print("Your guess is high.")
                wrong_guesses.append(guess)
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print("Your guesses:", guesses)
                print("Wrong guesses:", wrong_guesses)
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
if __name__ == "__main__":
    guessing_game()


