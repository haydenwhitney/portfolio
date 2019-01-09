#Hayden Whitney
#11/18
#A trivia word search game


import random

def tq1():
  q = "\nThe order of operations that python follows is this acronym. "
  ans = "PEMDAS"
  return q, ans

def tq2():
  q = "\nA number that is either a positive or negative whole number is an: "
  ans = "INTEGER"
  return q, ans

def tq3():
  q = "\nA floating decimal point number is a: "
  ans = "FLOAT"
  return q, ans

def tq4():
  q = "A _ stores a series of values that can be accessed through indexing or loops. "
  ans = "LIST"
  return q, ans

def tq5():
  q = "\nCode with human readable descriptions that can help document design decisions and has no affect on the execution of the code are called: "
  ans = "COMMENT"
  return q, ans

def tq6():
  q = "\nA named sequence of statements that will perform some useful operation is a: "
  ans = "FUNCTION"
  return q, ans

def tq7():
  q = "\nSymbols that perform mathematical operations (+, -, *, /) are known as: "
  ans = "OPERATORS"
  return q, ans

def tq8():
  q = "\nA _ statement tests a specified condition."
  ans = "IF"
  return q, ans

def tq9():
  q = "\nA _ allows you to access a particular part in a list. "
  ans = "SLICE"
  return q, ans

def tq10():
  q = "\nNames that store data are called: "
  ans = "VARIABLES"
  return q, ans
 
q_list = [tq1(), tq2(), tq3(), tq4(), tq5(), tq6(), tq7(), tq8(), tq9(), tq10()]
ans_list = "COMMENT, FLOAT, FUNCTION, IF, INTEGER, LIST, OPERATORS, PEMDAS, SLICE, VARIABLES"

puzzle = "NNOITCNUFSHXZINTEGEROTNEMMOCHOOQTVPTSILTZVAZECILSAEDOQMWCVBRBKLVDWXNUEAVFLAVGHMPXJFISLCCIOSELBAIRAVS"
polished_puzzle = """    0 1 2 3 4 5 6 7 8 9
  
0   N N O I T C N U F S
1   H X Z I N T E G E R
2   O T N E M M O C H O
3   O Q T V P T S I L T
4   Z V A Z E C I L S A
5   E D O Q M W C V B R
6   B K L V D W X N U E
7   A V F L A V G H M P
8   X J F I S L C C I O
9   S E L B A I R A V S
"""
def menu():
  print("[0] Tutorial")
  print("[1] Play")
  print("[2] Score")
  print("[3] Credits")
  choice = input("\nEnter the [#] of your choice: ")
  if choice == "0":
    tutorial()
  elif choice == "1":
    question()
  elif choice == "2":
    score()
  elif choice == "3":
    credits()
  else:
    print("Please enter a valid choice.")
    menu()

def credits():
  print("\nThis game was made possible by Matthew Walker, Hayden Whitney, and users like you. Thank you.")
  return_to_menu = input("\nPress the enter key to return to menu.\n")
  menu()

def random():
  q, ans = random.choice(q_list)
  return q, ans

def question():
  q, ans = random.choice(q_list)
  print("Remember Your answers can include")
  user_ans = input(q).upper()
  if user_ans == ans:
    search()
  else: 
    print("Please enter a valid answer.")
    

def search():
  print("Congrats! Now enter the index position of each letter in the word search.\n")
  user_pos = input("Your answer: ")
  print(polished_puzzle)
  


menu()