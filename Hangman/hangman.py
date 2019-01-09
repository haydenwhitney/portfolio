#Hayden Whitney
#11/18
#The classic game of hangman. the computer picks a random word
#and the player tries to guess it, one letter at a time. If the player
#can't guess the word in time, the little stick figure gets hanged.

import random

HANGMAN =("""
________
|     |
|     |
|
|
|
|
|
|
______________
""",
"""
________
|     |
|     |
|      O
|
|
|
|
|
______________
""",
"""
________
|     |
|     |
|      O
|      |
|      |
|
|
|
______________
""",
"""
________
|     |
|     |
|      O
|      |
|      |
|     /
|
|
______________
""",
"""
________
|     |
|     |
|      O
|      |
|      |
|     / \\
|
|
______________
""",
"""
________
|     |
|     |
|      O
|     /|
|      |
|     / \\
|
|
______________
""",
"""
________
|     |
|     |
|      O
|     /|\\
|      |
|     / \\
|
|
______________
""")
MAX_WRONG = len(HANGMAN)-1
#initialize variables
WORDS = ("PEMDAS", "FUNCTION", "INTEGER", "COMMENT", "FLOAT", "LIST", "OPERATORS", "IF", "SLICE", "SLICE", "VARIABLES")
word = random.choice(WORDS) #the word to be guessed
wrong = 0 #number of wrong guess player has made
used = []
so_far = "-" * len(word) #one dash for each letter n word to be guessed



def main():
    print("Welcome to Hangman. Good luck!")
    while wrong < MAX_WRONG and so_far != word:
        display(wrong)
    winner(wrong)

def display(wrong):
    print(HANGMAN[wrong])
    print("You've used the following letters: ", used)
    print("So far, the word is: ", so_far)
    user_input()
    
def user_input():
    guess = input("Enter your guess: ")
    guess = guess.upper()
    while guess in used:
        print("You've already guessed that letter.")
        guess = input("Enter your guess: ")
        guess = guess.upper()
    used.append(guess)
    check(guess, word)

def check(guess, word):
    global wrong
    global so_far
    so_far = so_far
    if guess in word:
        print("Yes!", guess, "is in the word!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
        return so_far
    else:
        print("Sorry,", guess, "isn't in the word.")
        wrong += 1

def winner(wrong):
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("You've been hanged!")
    else:
        print("You guessed it!")
        
main()
input("\n\n\nPress the enter key to exit.")    
