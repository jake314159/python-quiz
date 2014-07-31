import random
from random import shuffle
import sys

questions_to_ask = 16
questions = []

asked = 0
answer_correct = 0

def load_questions(file_name):
    print("loading "+file_name)
    ins = open( file_name, "r" )
    for line in ins:
        questions.append( line )
    ins.close()

def display_question(q):
    global asked
    global answer_correct
    asked += 1
    s = str(q).split(";")
    correct = s[1]
    print(s[0]) #Print the question
    s = s[1:]
    shuffle(s)

    # Print the answers
    for i in range(0,len(s)):
        print(str(i+1)+") "+(str(s[i]).rstrip('\n')))

    try:
        ans = int(input('->'))-1
    except ValueError:
        ans = -1

    if ans >= 0 and ans < len(s) and s[ans]==correct:
        print("\n\n------ CORRECT ------")
        answer_correct += 1
        return True
    else:
        print("\n\nWRONG IT'S '"+str(correct)+"'")
        return False;

# Load the questions
for arg in sys.argv[1:]:
    load_questions(arg)

q_range = list(range(len(questions)))
shuffle(q_range)
for i in range(1,questions_to_ask+1):
    print("\n\n\nQuestion "+str(i)+":")
    display_question(questions[q_range[i]])

print("\nYou got " + str(answer_correct) + " correct out of " + str(asked))

