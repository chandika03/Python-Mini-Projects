import random

print('------------Welcome to number guessing game--------------')
num1 = random.randint(1,10)

guess = 0
name = input("Enter your name:")

while guess<3:
    num2 = int(input("Enter the number:"))
    if num2 == num1:
        print(f"Great {name},You guessed it correctly 🎆")
        break
    else:
        print("The number is incorrect ❌")
        guess = guess + 1
if guess == 3 :
    print(f"Sorry, {name} but you are out of guesses. The correct number is {num1}👈🏼")