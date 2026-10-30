#(memory card game)
import random
import tkinter as tk
from tkinter import messagebox

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Game")
        self.colors = ["red", "orange", "yellow", "green", "turqoise", "blue", "purple", "pink"] * 2
random.shuffle(self.colors)
self.buttons = []
self.clicked_buttons = []
self.create_board()

def create_board(self):
    for i in range(4):

        for j in range(4):
            for i in range(4):
for j in range(4):
button = tk.Button(self.master, bg="gray", width=10, height=4, command=lambda row=i, col=j: self.flip(row, col))
button.grid(row=i, column=j)
self.buttons.append(button)
button.grid(row=i, column=j)
self.buttons.append(button)
def flip(self, row, col):
index = row * 4 + col
if self.buttons[index]["background"] != "gray" or len(self.clicked_buttons) >= 2:
return
self.buttons[index]["background"] = self.colors[index]
self.buttons[index].config(state=tk.DISABLED)
self.clicked_buttons.append((index, self.colors[index]))
if len(self.clicked_buttons) == 2:
self.check_match()
def check_match(self):
if self.clicked_buttons[0][1] == self.clicked_buttons[1][1]:
self.clicked_buttons = []
if all(button["background"] != "gray" for button in self.buttons):
messagebox.showinfo("Congratulations!", "You won!")
else:
self.master.after(1000, self.reset_tiles)

def reset_tiles(self):
for idx, _ in self.clicked_buttons:
self.buttons[idx]["background"] = "gray"
self.buttons[idx].config(state=tk.NORMAL)
self.clicked_buttons = []

def main():
    root = tk.Tk()
    MemoryGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
