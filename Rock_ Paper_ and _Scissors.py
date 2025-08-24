import tkinter as tk
import random

# === Score Variables ===
player_score = 0
computer_score = 0
tie_score = 0
round_count = 0
max_rounds = 5  # default

# === Choice symbols ===
CHOICES = {'r': "✊ Rock", 'p': "✋ Paper", 's': "✌️ Scissors"}

# === History List ===
history = []

# === Main Window ===
root = tk.Tk()
root.title("Rock Paper and Scissors!")           
root.geometry("760x750+440+150")
root.configure(bg = "#0f172a")

# === Top Labels ===
label = tk.Label(root, text="Rock · Paper · Scissors", font=("Roboto", 20, "bold"),
                 fg="#e2e8f0", bg="#0f172a")
label.pack(anchor="nw", padx=10, pady=(20, 0))

tittle = tk.Label(root, text="Pick your move or press keys: R (Rock), P (Paper), S (Scissors)",
                  fg="#e2e8f0", bg="#0f172a", font=("Roboto", 10, "bold"))
tittle.pack(anchor="nw", padx=10, pady=(5, 20))

# === Max Rounds Selector ===
round_frame = tk.Frame(root, bg="#0f172a")
round_frame.pack(pady=10)
round_label = tk.Label(round_frame, text="Select Max Rounds:", fg="white", bg="#0f172a", font=("Roboto",12,"bold"))
round_label.pack(side="left", padx=5)
round_var = tk.IntVar(value=max_rounds)
round_options = [2,5,7,10]
round_menu = tk.OptionMenu(round_frame, round_var, *round_options)
round_menu.config(width=5)
round_menu.pack(side="left", padx=5)

def set_max_rounds():
    global max_rounds, round_count
    max_rounds = round_var.get()
    round_count = 0
    reset_game()

set_round_button = tk.Button(round_frame, text="Set", command=set_max_rounds)
set_round_button.pack(side="left", padx=5)

# === Bottom Frame (Reset + Tip + History) ===
bottom_frame = tk.Frame(root, bg= "#0f172a")
bottom_frame.pack(side="bottom", fill="x", pady=10, padx=10)

reset_button = tk.Button(bottom_frame, width=12, height=2, text="Reset Game",
                         font=("Montserrat", 10, "bold"), bg="light gray")
reset_button.pack(side="left", anchor="sw")

# History Button
def show_history():
    hist_window = tk.Toplevel(root)
    hist_window.title("Game History")
    hist_window.geometry("400x400+600+200")
    hist_window.configure(bg="#0f172a")
    hist_label = tk.Label(hist_window, text="Game History", font=("Roboto", 14, "bold"), fg="white", bg="#0f172a")
    hist_label.pack(pady=10)
    listbox = tk.Listbox(hist_window, width=50, height=20, font=("Roboto", 10))
    listbox.pack(pady=10)
    for entry in history:
        listbox.insert(tk.END, entry)

history_button = tk.Button(bottom_frame, width=12, height=2, text="History",
                           font=("Montserrat", 10, "bold"), bg="light blue",
                           command=show_history)
history_button.pack(side="left", anchor="sw", padx=10)

tip = tk.Label(bottom_frame, text="Tip: Use R / P / S keys for quick play.",
               fg="#e2e8f0", bg="#0f172a")
tip.pack(side="right", anchor="se")

# === Button Frame ===
button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(side="bottom", pady=40)

button1 = tk.Button(button_frame, width=12, height=2, text="✊ Rock",
                    font=("Arial", 12, "bold"), fg="#0f172a", bg="#bac3cd")
button2 = tk.Button(button_frame, width=12, height=2, text="✋ Paper",
                    font=("Arial", 12, "bold"), fg="#0f172a", bg="#bac3cd")
button3 = tk.Button(button_frame, width=12, height=2, text="✌️ Scissors",
                    font=("Arial", 12, "bold"), fg="#0f172a", bg="#bac3cd")

button1.pack(side="left",  padx=(10,5), pady=20)
button2.pack(side="left",  padx=(5,5), pady=20)
button3.pack(side="left",  padx=(5,10), pady=20)

# === Result and Score Labels ===
result_label = tk.Label(root, text="", font=("Roboto", 14), fg="white", bg="#0f172a")
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Wins: 0 | Losses: 0 | Ties: 0 | Round: 0/{max_rounds}",
                       font=("Roboto", 14), fg="yellow", bg="#0f172a")
score_label.pack(pady=10)

# === Game Logic ===
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        return you == 'p'
    elif comp == 'p':
        return you == 's'
    elif comp == 's':
        return you == 'r'

# === Play function ===
def play(you):
    global player_score, computer_score, tie_score, history, round_count, max_rounds

    if round_count >= max_rounds:
        result_label.config(text=f"Max rounds reached! Game Over.", fg="orange")
        return

    comp = random.choice(["r", "p", "s"])
    a = gameWin(comp, you)

    comp_choice = CHOICES[comp]
    you_choice = CHOICES[you]

    # Increment round_count only if it's a win or loss
    if a is not None:
        round_count += 1

    if a is None:
        result_label.config(text=f"Computer chose {comp_choice}\nYou chose {you_choice}\n→ It's a Tie!", fg="yellow")
        tie_score += 1
        history.append(f"Tie: You {you_choice} | Computer {comp_choice}")
    elif a:
        result_label.config(text=f"Computer chose {comp_choice}\nYou chose {you_choice}\n→ You Win!", fg="green")
        player_score += 1
        history.append(f"Win: You {you_choice} | Computer {comp_choice}")
    else:
        result_label.config(text=f"Computer chose {comp_choice}\nYou chose {you_choice}\n→ You Lose!", fg="red")
        computer_score += 1
        history.append(f"Lose: You {you_choice} | Computer {comp_choice}")

    # Update scoreboard
    score_label.config(text=f"Wins: {player_score} | Losses: {computer_score} | Ties: {tie_score} | Round: {round_count}/{max_rounds}")

    # End game if max rounds reached
    if round_count >= max_rounds:
        if player_score > computer_score:
            result_label.config(text=result_label.cget("text") + "\nOverall Winner: You!")
        elif computer_score > player_score:
            result_label.config(text=result_label.cget("text") + "\nOverall Winner: Computer!")
        else:
            result_label.config(text=result_label.cget("text") + "\nOverall Result: Tie!")

# === Connect Buttons ===
button1.config(command=lambda: play("r"))
button2.config(command=lambda: play("p"))
button3.config(command=lambda: play("s"))

# === Reset function ===
def reset_game():
    global player_score, computer_score, tie_score, history, round_count
    player_score = computer_score = tie_score = round_count = 0
    history = []
    result_label.config(text="", fg="white")
    score_label.config(text=f"Wins: 0 | Losses: 0 | Ties: 0 | Round: 0/{max_rounds}")

reset_button.config(command=reset_game)

# === Keyboard handler ===
def key_handler(event):
    key = event.char.lower()
    if key in ["r","p","s"]:
        play(key)
    else:
        result_label.config(text=f"Invalid key: {event.char}\nPress R, P, or S only!", fg="orange")

root.bind("<Key>", key_handler)

root.mainloop()
