import random
import tkinter as tk
from tkinter import PhotoImage, Label, Button
import os

# Get the current directory path
current_path = os.path.dirname(os.path.abspath(__file__))
dice_folder_path = os.path.join(current_path, "Dice")

# Function to roll the dice
def roll_dice():
    number = random.randint(1, 6)
    dice_label.config(image=dice_images[number-1])

# Setting up the main GUI window
root = tk.Tk()
root.title("Dice Simulation")

# Load dice images
dice_images = [
    PhotoImage(file=os.path.join(dice_folder_path, f'dice{num}.png')) for num in range(1, 7)
]

dice_label = Label(root, image=dice_images[0])  # default to dice face 1
dice_label.pack(pady=20)

roll_btn = Button(root, text="Roll the Dice", command=roll_dice)
roll_btn.pack()

exit_btn = Button(root, text="Exit", command=root.quit)
exit_btn.pack(pady=20)

root.mainloop()
