import random
game = "x"
game_on = "yes"
replay = "yes"
guessing = "yes"
print("Computer Programming Hangman!")


print("Please answer with Yes or No on Yes or No questions.")
print("Please answer with only letters during guessing letters")
print("Please answer with the full word when guessing the word")
print()




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
        print("The word has "+str(x)+" letters to guess.")
        print("Answer \"letter\" or \"word\"")
        choice_uno = input("Guess a letter or Guess the full word? ")
        if choice_uno == "letter" or choice_uno == "Letter":
            choice_letter = input("What letter would you like to guess? ")
        
        elif choice_uno == "word" or choice_uno == "Word":
            choice_word = input("Type out the word you'd like to guess! ")

    


    break