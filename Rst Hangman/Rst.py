import random
game = "x"
game_on = "yes"
replay = "yes"
guessing = "yes"
guesses = 6
winner = "undecided"
try_again = "y"
word_guessed = "b"
print("Computer Programming Hangman!")


print("Please answer with Yes or No on Yes or No questions.")
print("Please answer with only letters during guessing letters")
print("Please answer with the full word when guessing the word")
print()

def bodypart(g):
    print('     --------')
    print('     |       ' + ('|' if guesses <= 6 else ''))
    print('     |       ' + ('O' if guesses <= 5 else ''))
    print('     |     ' +(' / \\' if guesses <= 4 else ''))
    print('     |       ' + ('|' if  guesses <=3 else '' ))
    print('     |       ' + ('|' if guesses <= 2 else ''))
    print('     |     '+(' / \\' if guesses <=1 else ''))
    print(' --------   ')
    



#List of Words
word_selection = ["PYTHON","ARRAY","LOOPS","BINARY","PROGRAM","PROGRAMMING","STRING","PRINT", "HTML", "JAVASCRIPT", "COMPUTER", "CODE", "LANGUAGE","KEYBOARD","MOUSE","MONITER", "TECHNOLOGY","VARIABLE","INPUT","FLOAT","STATMENT","ERROR","OUTPUT","DEBUG","TERINAL","SOURCE","ROBOT","ARTIFICIAL","ETHERENET","INTERNET","ROUTER","GRAPHICS","FUNCTION","IMPORT","EXPORT","CONDITIONS","INDEX","TUUPLES","OPERATORS","BOOLEANS","COMMENTS","MODULES","ANALYITICS","SYNTAX","LIST","INFORMATION","EXTENTIONS","CONTROL","SERVER",]




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
print()

word = list(random.choice(word_selection))
visible_word = []
ex_word = "".join(word)
print(ex_word)

for character in word:
    visible_word.append('_')


while guessing == "yes":
    if  word_guessed == "yes":
        guessing = "end"
        winner = "won"
        break
    elif guesses == 0:
        guessing = 'end'
        winner = "lost"
        break
    elif word == visible_word:
        guessing = "end"
        winner = "won"
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
        choice_word = choice_word.upper()
        if choice_word == ex_word:
            print("You Guessed The Word! You still had "+str(guesses)+"left")
            print()
            guessing = "won"
            winner = "won"
            word_guessed = "yes"

            break
        elif choice_word != ex_word:
            print("You guessed Incorrectly! \""+str(choice_word)+"\" Is not the word!")
            guesses -= 1
            print("That's a guess lost! You have "+str(guesses)+" left! Uh oh!")
            continue
               
                
                

            
    else:
        print("Please type either \"word\" or \"letter\" depending on your choice.")



if winner == "lost":
    print("Oh you lost! Too bad... You may not have have won but were proud you tried.")
    print("The word was"+str(ex_word))
    

elif winner == "won":
    print("Oh wow! you guessed the word! Congratulations are in order go tell your friends that you won hangman good job.")
    print("The word was"+ str(ex_word))
    