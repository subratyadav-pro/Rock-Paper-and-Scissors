import tkinter as tk
import random

randNumber = random.randint(1, 100)
guesses = 0
highscore = None

def check_guess():
    global guesses, highscore, randNumber
    try:
        userGuess = int(entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number!")
        return

    guesses += 1
    if userGuess == randNumber:
        result_label.config(text=f"You guessed it right in {guesses} tries!")
        if highscore is None or guesses < highscore:
            highscore = guesses
            highscore_label.config(text=f"High Score: {highscore}")
    elif userGuess > randNumber:
        result_label.config(text="Try a smaller number")
    else:
        result_label.config(text="Try a larger number")

def restart_game():
    global randNumber, guesses
    randNumber = random.randint(1, 100)
    guesses = 0
    result_label.config(text="")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Guess the Number")
root.geometry("300x200")

tk.Label(root, text="Guess a number (1-100):").pack(pady=5)
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=check_guess).pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

highscore_label = tk.Label(root, text="High Score: None")
highscore_label.pack(pady=5)

tk.Button(root, text="Restart", command=restart_game).pack(pady=5)

root.mainloop()
