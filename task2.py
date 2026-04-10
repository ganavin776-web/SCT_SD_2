import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import random

# Game logic
number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess > number:
            result_label.config(text="Too High 🔺", fg="#ff6b6b")
        elif guess < number:
            result_label.config(text="Too Low 🔻", fg="#4dabf7")
        else:
            result_label.config(
                text=f"🎉 Correct in {attempts} attempts!", fg="#51cf66"
            )
    except:
        result_label.config(text="Enter valid number!", fg="orange")

def restart_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="Game Restarted 😄", fg="white")

# Window
root = tk.Tk()
root.title("Guess The Number")
root.state("zoomed")

# Screen size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Background image
bg = Image.open("bg1.png").resize((width, height))

# Blur + dim
bg = bg.filter(ImageFilter.GaussianBlur(4))
enhancer = ImageEnhance.Brightness(bg)
bg = enhancer.enhance(0.6)

bg_photo = ImageTk.PhotoImage(bg)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 🔥 MATCHING COLOR (important for blending)
bg_color = "#3a3a3a"

# Title
title = tk.Label(
    root,
    text="🎯 Guess The Number",
    font=("Arial", 26, "bold"),
    bg=bg_color,
    fg="white"
)
title.place(relx=0.5, rely=0.35, anchor="center")

# Instruction
instruction = tk.Label(
    root,
    text="Enter number (1–100)",
    font=("Arial", 16),
    bg=bg_color,
    fg="#dddddd"
)
instruction.place(relx=0.5, rely=0.42, anchor="center")

# Entry (blended)
entry = tk.Entry(
    root,
    font=("Arial", 18, "bold"),
    justify="center",
    bg=bg_color,
    fg="white",
    insertbackground="white",
    bd=0,
    highlightthickness=0,
    relief="flat",
    width=10
)
entry.place(relx=0.5, rely=0.48, anchor="center")

# Check button
check_btn = tk.Button(
    root,
    text="Check",
    font=("Arial", 12, "bold"),
    command=check_guess,
    bg="#4CAF50",
    fg="white",
    bd=0
)
check_btn.place(relx=0.5, rely=0.56, anchor="center")

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg=bg_color,
    fg="white"
)
result_label.place(relx=0.5, rely=0.63, anchor="center")

# Restart button
restart_btn = tk.Button(
    root,
    text="Restart",
    font=("Arial", 12, "bold"),
    command=restart_game,
    bg="#ff4d4d",
    fg="white",
    bd=0
)
restart_btn.place(relx=0.5, rely=0.70, anchor="center")

root.mainloop()