import random
game = "x"
print("Computer Programming Hangman!")


print("Please answer with Yes or No on Yes or No questions.")
print("Please answer with only letters during guessing letters")
print("Please answer with the full word when guessing the word")
print()

while game == "x":
    start = input("Read the Rules? ")
    if start == 'yes' or start == "Yes" or start == "y" or start == "Y":
        print("The object of hangman is to guess the secret word or words before the stick figure is hung. You will take turns selecting letters to narrow the word down. Players can take turns or guess the word at any time yet a failure of a guess results in a body part of the man being hung. Gameplay continues until the players guess the word or they run out of guesses and the stick figure is hung.")
        print()
        break
    elif start == 'no' or start == "No" or start == "n" or start == "N":
        print("Alright let's get started!")
    else:
        print("Please answer with Yes or No...")