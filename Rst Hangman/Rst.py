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
    print('     ------')
    print('     |       ' + ('|' if guesses <= 6 else ''))
    print('     |       ' + ('O' if guesses <= 5 else ''))
    print('     |      ' +(' /\\' if guesses <= 4 else ''))
    print('     |        ' + ('|' if  guesses <=3 else '' ))
    print('     |        ' + ('|' if guesses <= 2 else ''))
    print('     |      '+('/\\' if guesses <=1 else ''))
    print(' --------   ')
    



#List of Words
word_selection = ["PYTHON","ARRAY","LOOPS","BINARY","PROGRAM","PROGRAMMING","STRING","PRINT", "HTML", "JAVASCRIPT", "COMPUTER", "CODE", "LANGUAGE","KEYBOARD","MOUSE","MONITER", "TECHNOLOGY","VARIABLE","INPUT","FLOAT","STATMENT","ERROR","OUTPUT","DEBUG","TERINAL","SOURCE","ROBOT","ARTIFICIAL","ETHERENET","INTERNET","ROUTER","GRAPHICS","FUNCTION","IMPORT","EXPORT","CONDITIONS","INDEX","TUUPLES","OPERATORS","BOOLEANS","COMMENTS","MODULES","ANALYITICS","SYNTAX","LIST","INFORMATION","EXTENTIONS","CONTROL","SERVER",]


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

    word = list(random.choice(word_selection))
    visible_word = []
    for character in word:
        visible_word.append('_')


    while guessing == "yes":
        if visible_word == word:
            game = "end"
            break
        elif guesses == 0:
            game = 'end'
            break
        print(visible_word)
        print("Answer \"letter\" or \"word\"")
        bodypart(guesses)
        choice_uno = input("Guess a letter or Guess the full word? ")
        if choice_uno == "letter" or choice_uno == "Letter":
            choice_letter = input("What letter would you like to guess? ")
            choice_letter = choice_letter.upper()
            if choice_letter in word:
                print("You guessed correctly! \""+str(choice_letter)+"\" Is in the word!")
                for i in range( len(word) ):
                    character = word[i]
                    if character == choice_letter:
                        visible_word[i] = word[i]
                        word[i] = "_"
            elif choice_letter not in word:
                print("You guessed Incorrectly! \""+str(choice_letter)+"\" Is not in the word!")
                guesses -= 1
                print("That's a guess lost! You have "+str(guesses)+" left! Uh oh!")
                continue
            

        
        elif choice_uno == "word" or choice_uno == "Word":
            choice_word = input("Type out the word you'd like to guess! ")
            if choice_word == word:
                print("You Guessed The Word! You still had "+str(guesses)+"left")
                game = "won"
                break
            else:
                print("You guessed Incorrectly! \""+str(choice_letter)+"\" Is not in the word!")
                guesses -= 1
                print("That's a guess lost! You have "+str(guesses)+" left! Uh oh!")
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