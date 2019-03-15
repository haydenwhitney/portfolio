# Hayden Whitney
# 3/19
# D & D Companion

from tkinter import *
import random


class Player(object):
    def __init__(self):
        self.name = ""
        self.level = 1
        self.current_exp = 0
        self.inventory = []

    def add_item(self):
        pass

    def add_exp(self):
        pass

    def use_item(self):
        pass


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.player = Player()
        self.grid()
        self.create_widgets()
        self.exp = 0

    def create_widgets(self):
        self.level_label = Label(self, text="Level:")
        self.level_label.grid(row=1, column=1, sticky=W)

        self.exp_label = Label(self, text="Total Experience:")
        self.exp_label.grid(row=2, column=1, sticky=W)

        self.inventory = Label(self, text="Inventory:")
        self.inventory.grid(row=3, column=1, sticky=W)
        self.inventory_input = Entry(self)
        self.inventory_input.grid(row=4, column=2, columnspan=3)
        self.add = Button(self, text="Add", command=self.add)
        self.add.grid(row=5, column=4, sticky=E)

        self.instructions = Label(self, text="Click to roll:")
        self.instructions.grid(row=6, column=1, sticky=W)

        self.d4 = Button(self, text="D4", width=5, height=2, command=self.d4)
        self.d4.grid(row=7, column=1, sticky=E)
        self.d4_output = Text(self, width=5, height=2)
        self.d4_output.grid(row=8, column=1, sticky=E)

        self.d6 = Button(self, text="D6", width=5, height=2, command=self.d6)
        self.d6.grid(row=7, column=2, sticky=W + E)
        self.d6_output = Text(self, width=5, height=2)
        self.d6_output.grid(row=8, column=2, sticky=W+E)

        self.d8 = Button(self, text="D8", width=5, height=2, command=self.d8)
        self.d8.grid(row=7, column=3, sticky=W + E)
        self.d8_output = Text(self, width=5, height=2)
        self.d8_output.grid(row=8, column=3, sticky=W+E)

        self.d10 = Button(self, text="D10", width=5, height=2, command=self.d10)
        self.d10.grid(row=7, column=4, sticky=W + E)
        self.d10_output = Text(self, width=5, height=2)
        self.d10_output.grid(row=8, column=4, sticky=W+E)

        self.d12 = Button(self, text="D12", width=5, height=2, command=self.d12)
        self.d12.grid(row=7, column=5, sticky=W + E)
        self.d12_output = Text(self, width=5, height=2)
        self.d12_output.grid(row=8, column=5, sticky=W+E)

        self.d20 = Button(self, text="D20", width=5, height=2, command=self.d20)
        self.d20.grid(row=7, column=6, sticky=W + E)
        self.d20_output = Text(self, width=5, height=2)
        self.d20_output.grid(row=8, column=6, sticky=W+E)

    def exp(self):
        add = int(input("Enter the amount of experience points earned: "))
        self.exp += add
        if 0 > self.exp < 300:
            level = 1
            proficiency_bonus = 2
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 300 <= self.exp < 900:
            level = 2
            proficiency_bonus = 2
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 900 <= self.exp < 2700:
            level = 3
            proficiency_bonus = 2
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 2700 <= self.exp < 6500:
            level = 4
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 6500 <= self.exp < 14000:
            level = 5
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 14000 <= self.exp < 23000:
            level = 6
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 23000 <= self.exp < 34000:
            level = 7
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 34000 <= self.exp < 48000:
            level = 8
            proficiency_bonus = 3
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 48000 <= self.exp < 64000:
            level = 9
            proficiency_bonus = 4
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 64000 <= self.exp < 85000:
            level = 10
            proficiency_bonus = 4
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 85000 <= self.exp < 100000:
            level = 11
            proficiency_bonus = 4
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 100000 <= self.exp < 120000:
            level = 12
            proficiency_bonus = 4
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 120000 <= self.exp < 140000:
            level = 13
            proficiency_bonus = 5
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 140000 <= self.exp < 165000:
            level = 14
            proficiency_bonus = 5
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 165000 <= self.exp < 195000:
            level = 15
            proficiency_bonus = 5
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 195000 <= self.exp < 225000:
            level = 16
            proficiency_bonus = 5
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 225000 <= self.exp < 265000:
            level = 17
            proficiency_bonus = 6
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 265000 <= self.exp < 305000:
            level = 18
            proficiency_bonus = 6
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif 305000 <= self.exp < 355000:
            level = 19
            proficiency_bonus = 6
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
        elif self.exp >= 355000:
            level = 20
            proficiency_bonus = 6
            print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")

    def add(self):
        pass

    def d4(self):
        self.d4_output.delete(0.0, END)
        self.d4_output.insert(0.0, random.randint(1, 4))

    def d6(self):
        self.d6_output.delete(0.0, END)
        self.d6_output.insert(0.0, random.randint(1, 6))

    def d8(self):
        self.d8_output.delete(0.0, END)
        self.d8_output.insert(0.0, random.randint(1, 8))

    def d10(self):
        self.d10_output.delete(0.0, END)
        self.d10_output.insert(0.0, random.randint(1, 10))

    def d12(self):
        self.d12_output.delete(0.0, END)
        self.d12_output.insert(0.0, random.randint(1, 12))

    def d20(self):
        self.d20_output.delete(0.0, END)
        self.d20_output.insert(0.0, random.randint(1, 20))


root = Tk()
root.title("D & D Companion")
# root.geometry("375x200")
app = Application(root)
root.mainloop()
