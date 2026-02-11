import random


print("Welcome to ROCK PAPER SCISSOR game")
print("Rules\n 1.Rock🪨 wins Scissor✂️\n2. Paper📃 wins Rock🪨\n3.Scissor✂️ wins Paper📃")
while True:
    print("1. Rock 2. Paper 3. Scissor")
    choice = int(input("Enter you choice (1,2,3):"))
    if choice == 1:
        print("You chose rock🪨")
    elif choice == 2:
        print("You chose Paper 📃")
    elif choice == 3:
        print("You chose scissor ✂️")
    else:
        print("Invalid number, please choose a number between 1-3")

    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        print("Computer chose Rock")
    elif computer_choice == 2:
        print("Computer chose Paper 📃")
    elif computer_choice == 3:
        print("Computer chose scissor ✂️")

    if choice == computer_choice:
        print("DRAW")
    elif (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 3) or (choice == 3 and computer_choice == 1):
        print("Computer won 💀")
    elif (computer_choice == 1 and choice == 2) or (computer_choice == 2 and choice == 3) or (computer_choice == 3 and choice == 1):
        print("You won ❤️")

    again = input("Do you want to play again? (Y/N) ")
    ans = again.lower()
    if ans == 'n':
        break

print("Thanks for playing")