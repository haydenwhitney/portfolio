#Hayden Whitney
#9/18
#Change Sorter

def change():
    total_change = int(input("How much change do you have? "))
    quarters = total_change // 25
    leftovers = total_change % 25
    dimes = leftovers // 10
    leftovers = leftovers % 10
    nickels = leftovers // 5
    leftovers = leftovers % 5
    cents = leftovers // 1
    leftovers = leftovers
    #3 display it back to the user
    print("Quarters: ", quarters, "\nDimes: ", dimes, "\nNickels: ", nickels, "\nCents: ", cents)

change()

def change2(total_change):
    total_change = total_change
    quarters = total_change // 25
    leftovers = total_change % 25
    dimes = leftovers // 10
    leftovers = leftovers % 10
    nickels = leftovers // 5
    leftovers = leftovers % 5
    cents = leftovers // 1
    leftovers = leftovers
    return quarters, dimes, nickels, cents

total_change = int(input("How much change do you have? "))
quarters, dimes, nickels, cents = change2(total_change)
print("Quarters: ", quarters, "\nDimes: ", dimes, "\nNickels: ", nickels, "\nCents: ", cents)
    
    

