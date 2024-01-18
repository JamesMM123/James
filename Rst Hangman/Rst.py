import random
game = "x"
game_on = "yes"
replay = "yes"
guessing = "yes"
guesses = 6
winner = "undecided"
print("Computer Programming Hangman!")


print("Please answer with Yes or No on Yes or No questions.")
print("Please answer with only letters during guessing letters")
print("Please answer with the full word when guessing the word")
print()

def bodypart(g):
    if g == 5:
        print("The head is drawn")

    elif g == 4:
        print("The Body is drawn ")
    elif g == 3:
        print("The Left Leg is drawn")

    elif g == 2:
        print("The Right Leg is drawn")

    elif g == 1:
        print("The Left Arm is drawn")

    elif g == 0:
        print("The Right Arm is drawn")
        winner = "lost"
    


#List of Words
word_selection = ["Python","Array","Loops","Binary","Programming","Program","String","Print", "If/Elif/Else", "HTML", "Javascript", "Computer", "Code", "Language","Keyboard","Mouse","Moniter", "Technology","Variable","Input","Float","Statement","Error","Output","Debug","Terminal","Source","Robot","Artificial","Ethernet","Internet","Router","Graphics","Function","Import","Export","Conditions","Index","Tuples","Operators","Booleans","Comments","Modules","Analyitics","Syntax","List","Information","Extensions","Control","Server", ]


while replay == "yes":

    while game == "x":
        start = input("Read the Rules? ")
        if start == 'yes' or start == "Yes" or start == "y" or start == "Y":
            print("The object of hangman is to guess the secret word or words before the stick figure is hung. You will take turns selecting letters to narrow the word down. Players can take turns or guess the word at any time yet a failure of a guess results in a body part of the man being hung. Gameplay continues until the players guess the word or they run out of guesses and the stick figure is hung.")
            print()
            print("Now that we've read the rules lets play!")
            print()
            game = "c"
            break
    
        elif start == 'no' or start == "No" or start == "n" or start == "N":
            print("Alright let's get started!")
            print()
            game = "c"
            break
        else:
            print("Please answer with Yes or No...")
            print()
    print("The computer is deciding what word for you to guess!")
    print("The computer has decided!")
    choice = random.choice(word_selection)
    x = len(choice)
    y = "_ "

    while guessing == "yes":
        print(str(y * x))
        print("The word has "+str(x)+" letters unguessed.")
        print("Answer \"letter\" or \"word\"")
        choice_uno = input("Guess a letter or Guess the full word? ")
        if choice_uno == "letter" or choice_uno == "Letter":
            choice_letter = input("What letter would you like to guess? ")
            if choice_letter in choice:
                print("You guessed correctly!")
                for choice_letter in choice:
                    choice.find(choice_letter)
                    choice.replace(choice_letter, '')
                
            

        
        elif choice_uno == "word" or choice_uno == "Word":
            choice_word = input("Type out the word you'd like to guess! ")
            if choice_word == choice:
                print("You Guessed The Word! You still had "+str(guesses)+"left")
                game = "won"
                break
            else:
                print("Incorrect Your lost 1 guess")
                guesses -= 1
                print("You now have "+str(guesses)+" left!")
                bodypart(guesses)
                continue
               
                
                

            
        else:
            print("Please type either \"word\" or \"letter\" depending on your choice.")



    if winner == "lost":
        try_again = input("You lost would you like to try again")
        if try_again == "yes" or try_again == "Yes" or try_again == "y" or try_again == "yer":
            continue
        elif try_again == "no" or try_again == "No" or try_again == "n" or try_again == "Nuh uh" or try_again == "nuh uh":
            print("Okkie Dokkie")

    elif winner == "won":
        try_again == input("Wow! You won would you like to try again?")
        if try_again == "yes" or try_again == "Yes" or try_again == "y" or try_again == "Y" or try_again == "yer" or try_again == "yer":
            continue
        elif try_again == "no" or try_again == "No" or try_again == "n" or try_again == "Nuh uh" or try_again == "nuh uh":
            print("Okey Dookie")