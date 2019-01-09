#Hayden Whitney
#12/18
#Yu-Gi-Oh Campanion Program

def main():
  print("""
[0] DUEL
[1] CREDITS
[2] EXIT
  """)
  choice = input("Enter the [#] of your choice: ")
  if choice == "0":
    calculate_lp()
  elif choice == "1":
    credits()
  elif choice == "2":
    exit()
  else:
    print("\nPlease enter a valid choice.")
    main()

def welcome():
  print("""WELCOME TO YOUR NEW YU-GI-OH COMPANION!""")

def credits():
  print("This program was made possible by Hayden Whitney and users like you. Thank you.")
  main()

def exit():
  choice = input("Are you sure? [Y]/[N]: ").title()
  while True:
    if choice == "Yes" or choice == "Ye" or choice =="Y":
      break
    else:
      main()

def get_names():
  player_1 = input("\nEnter a name for Player 1: ").upper()
  player_2 = input("Enter a name for Player 2: ").upper()
  choice = input("Are you sure? [Y]/[N]: ").upper()
  while True:
    if choice == "Yes" or choice == "Ye" or choice =="Y":
      return player_1, player_2
      break
    elif choice == "No" or choice == "N":
      get_names()
    else:
      print("\nPlease enter a valid choice.")
      get_names()

def calculate_lp():
  player_1_lp = 8000
  player_2_lp = 8000
  player_1, player_2 = get_names()
  while True:
    if player_1_lp <= 0:
      print("")
      print(player_1.title(), "loses and", player_2.title(), "prevails!")
      input("\nPress the enter key to exit.")
      break
    elif player_2_lp <= 0:
      print("")
      print(player_2.title(), "loses and", player_1.title(), "prevails!")
      input("\nPress the enter key to exit.")
      break
    else:
      print("""
[+] ADD
[-] SUBTRACT
      """)
      choice = input("Enter the [operator] of your choice: ")
      if choice == "+":
        print("\n[1]", player_1, "\n[2]", player_2)
        choice = input("\nEnter the [#] of your choice: ")
        if choice == "1":
          lp = input("\nEnter the amount of LP to be added: ")
          lp = int(lp)
          player_1_lp = player_1_lp + lp
        elif choice == "2":
          lp = input("\nEnter the amount of LP to be added:")
          lp = int(lp)
          player_2_lp = player_2_lp + lp
        else:
          print("Please enter a valid choice.")
          continue
      elif choice == "-":
        print("\n[1]", player_1, "\n[2]", player_2)
        choice = input("\nEnter the [#] of your choice: ")
        if choice == "1":
          lp = input("\nEnter the amount of LP to be subtracted: ")
          lp = int(lp)
          player_1_lp = player_1_lp - lp
        elif choice == "2":
          lp = input("\nEnter the amount of LP to be subtracted: ")
          lp = int(lp)
          player_2_lp = player_2_lp - lp
        else:
          print("Please enter a valid choice.")
          continue
      else:
        print("Please enter a valid choice.")
        continue
      print("")
      print(player_1, ":")
      print(player_1_lp)
      print("")
      print(player_2, ":")
      print(player_2_lp)
      

welcome()
main()