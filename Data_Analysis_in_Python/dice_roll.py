
import tkinter as tk
import random


def roll_dice():
    dice_number = random.randint(1, 6)
    dice_label.config(text=f"🎲 You rolled: {dice_number}")


root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x200")
root.config(bg="#1e1e1e")  


heading = tk.Label(root, text="Dice Roller 🎲", font=("Arial", 18, "bold"), fg="cyan", bg="#1e1e1e")

heading.pack(pady=10)
dice_label = tk.Label(root, text="Press Roll to start", font=("Arial", 14), fg="white", bg="#1e1e1e")
dice_label.pack(pady=20)


roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 12, "bold"), fg="white", bg="purple", command=roll_dice)
roll_button.pack(pady=10)


root.mainloop()
