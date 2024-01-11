print("Time for a quiz!")
print("Please answer with A, B, C or D for multiple choice questions")
print("Also remember to type the number for example \"Two\" ")
print("Only answer with a value number if asked specifically in a math question")
print()

counter= 0
questions = "unanswered"
while questions == "unanswered":
    q1 = input("Best video game series? A. Call of Duty B. Halo C. Madden D. The Last of us ")
    if q1 == "b" or q1 == "B":
        print("Correct! You have great taste!")
        print()
        counter += 1
        break
    elif q1 == "a" or q1 == "A" or q1 == "c" or q1 == "C" or q1 == "d" or q1 == "D":
        print("I respect your opinion but no, that's incorrect. ")
        print()
        break
    else:
        print("That wasn't even an answer. Try again. ")
        print("Please answer with A, B, C or D for multiple choice questions")
        print()
        continue

while questions == "unanswered":
    q2 = input("What year was the last time the leafs won the cup? A.2002 B.1997 C.1972 D.1967 ")
    if q2 == "d" or q1 == "D":
        print("That's Correct! Is that a good or bad thing?")
        print()
        counter += 1
        break
    elif q2 == "a" or q2 == "A" or q2 == "c" or q2 == "C" or q2 == "b" or q2 == "B":
        print("Haha no. Very incorrect.")
        print()
        break
    else:
        print("That wasn't even an answer. Try again. ")
        print("Please remember to answer with A, B, C or D for multiple choice questions")
        print()
        continue
    
    print()
while questions == "unanswered":
    q3 = input("Which of these people were apart of the beetles? A. John Lennon B. Katy Perry C. Elvis Presley D. Bill Gates ")
    if q3 == "a" or q1 == "A":
        print("That's Correct! I'd be suprised if you chose anyone else...")
        print()
        counter += 1
        break
    elif q3 == "D" or q3 == "D" or q3 == "c" or q3 == "C" or q3 == "b" or q3 == "B":
        print("That was way too easy for you to fail. Incorrect.")
        print()
        break
    else:
        print("That wasn't even an answer. Try again.")
        print("Please remember to answer with A, B, C or D for multiple choice questions")
        print()
        continue

    print()
    
while questions == "unanswered":
    q4 = input("How many band members were in the One direction band? ")
    if q4 == "5" or q4 == "five" or q4 == "Five":
        print("You got that right? That's pretty odd...")
        print()
        counter += 1
        break
    else:
        print("I don't blame you for getting this wrong. Who really cares? I know I don't.")
        print()
        break

while questions == "unanswered":
    q5 = input("Last question. 13 + ( 7 x ((2**4) / 2) - 2)? ")
    if q5 == "67" or q5 == "sixty seven" or q5 == "Sixty Seven" or q5 == "sixteyseven" or q5 == "Sixteyseven" or q5 == "SixteySeven":
        print("Correct. Took you long enough.")
        print()
        counter += 1
        break
    else:
        print("All of that work just to fail a math question...")
        print()
        break

print("Congrats! You got "+str(counter)+" questions right!")
percentscore = counter / 5 * 100
print("That's %"+str(percentscore)+" percent.")

if percentscore == 100:
    print("All of them? You either cheated or you're lucky.")
elif percentscore == 80:
    print("Almost all of em. You could have gotten them all though....")
elif percentscore == 60:
    print("Just above half. Not bad but Not good.")
elif percentscore == 40:
    print("Youch. You could definitely do better.")
elif percentscore == 20:
    print("How do you only get one right?! That was a bad attempt not going to lie.")
elif percentscore == 0:
    print("I hate to be rude but either you failed on purpose or you're really stupid.")

print("Hello")