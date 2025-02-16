import tkinter as tk
from tkinter import ttk

def calculate_scores():
    # ----------------------
    # AWAY Team calculations
    # ----------------------
    possessions_per_game = 10.5
    total_score = 0

    # 1) Grade the Offense
    away_grade = away_grade_var.get()
    if away_grade == "A":
        points_per_possession = 5.5
    elif away_grade == "B":
        points_per_possession = 4.5
    elif away_grade == "C":
        points_per_possession = 3.5
    elif away_grade == "D":
        points_per_possession = 2.5
    else:
        points_per_possession = 0  # fallback if nothing selected

    # 2) Turns ball over near scoring position? (Yes/No)
    away_turns_over = away_turns_var.get()
    if away_turns_over == "Yes":
        possessions_per_game -= 1.5
    else:  # "No"
        total_score += 1

    # 3) Gets Takeaway from opponent near scoring position? (Yes/No)
    away_gets_turnover = away_gets_turnover_var.get()
    if away_gets_turnover == "Yes":
        possessions_per_game += 1
        total_score += 1

    # 4) Wins ToP? (Yes/No)
    away_wins_top = away_wins_top_var.get()
    if away_wins_top == "Yes":
        total_score += 1
    else:  # "No"
        possessions_per_game -= 0.5

    # 5) Calculate final score for AWAY team
    away_final = ((possessions_per_game * points_per_possession) + total_score) * 0.58
    away_score_var.set(f"{away_final:.2f}")

    # ----------------------
    # HOME Team calculations
    # ----------------------
    possessions_per_game = 10.5
    total_score = 0

    # 1) Grade the Offense
    home_grade = home_grade_var.get()
    if home_grade == "A":
        points_per_possession = 5.5
    elif home_grade == "B":
        points_per_possession = 4.5
    elif home_grade == "C":
        points_per_possession = 3.5
    elif home_grade == "D":
        points_per_possession = 2.5
    else:
        points_per_possession = 0

    # 2) Turns ball over? (Yes/No)
    home_turns_over = home_turns_var.get()
    if home_turns_over == "Yes":
        possessions_per_game -= 1.5
    else:
        total_score += 1

    # 3) Gets Turnover? (Yes/No)
    home_gets_turnover = home_gets_turnover_var.get()
    if home_gets_turnover == "Yes":
        possessions_per_game += 1
        total_score += 1

    # 4) Wins ToP? (Yes/No)
    home_wins_top = home_wins_top_var.get()
    if home_wins_top == "Yes":
        total_score += 1
    else:
        possessions_per_game -= 0.5

    # 5) Calculate final score for HOME team
    home_final = ((possessions_per_game * points_per_possession) + total_score) * 0.575
    home_score_var.set(f"{home_final:.2f}")


def reset_fields():
    """
    Reset all combo boxes to defaults and clear the final score labels.
    """
    away_grade_var.set("A")
    away_turns_var.set("Yes")
    away_gets_turnover_var.set("No")
    away_wins_top_var.set("No")
    away_score_var.set("")

    home_grade_var.set("A")
    home_turns_var.set("Yes")
    home_gets_turnover_var.set("No")
    home_wins_top_var.set("No")
    home_score_var.set("")

# ----------------------
# Build the Tkinter GUI
# ----------------------
root = tk.Tk()
root.title("Final Score Approx Calculator")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid()

# Column headers: AWAY, HOME
ttk.Label(main_frame, text="AWAY", font=('Arial', 10, 'bold')).grid(row=0, column=1, padx=5)
ttk.Label(main_frame, text="HOME", font=('Arial', 10, 'bold')).grid(row=0, column=2, padx=5)

# 1) Grade the Offense
ttk.Label(main_frame, text="Grade the Offense:").grid(row=1, column=0, sticky=tk.E, pady=2)
away_grade_var = tk.StringVar(value="A")
away_grade_cb = ttk.Combobox(main_frame, textvariable=away_grade_var, 
                             values=["A", "B", "C", "D"], state="readonly")
away_grade_cb.grid(row=1, column=1, padx=5, pady=2)

home_grade_var = tk.StringVar(value="A")
home_grade_cb = ttk.Combobox(main_frame, textvariable=home_grade_var, 
                             values=["A", "B", "C", "D"], state="readonly")
home_grade_cb.grid(row=1, column=2, padx=5, pady=2)

# 2) Turns ball over?
ttk.Label(main_frame, text="Commits Turnover?").grid(row=2, column=0, sticky=tk.E, pady=2)
away_turns_var = tk.StringVar(value="Yes")
away_turns_cb = ttk.Combobox(main_frame, textvariable=away_turns_var, 
                             values=["Yes", "No"], state="readonly")
away_turns_cb.grid(row=2, column=1, padx=5, pady=2)

home_turns_var = tk.StringVar(value="Yes")
home_turns_cb = ttk.Combobox(main_frame, textvariable=home_turns_var, 
                             values=["Yes", "No"], state="readonly")
home_turns_cb.grid(row=2, column=2, padx=5, pady=2)

# 3) Gets Turnover?
ttk.Label(main_frame, text="Defensive Takeaway?").grid(row=3, column=0, sticky=tk.E, pady=2)
away_gets_turnover_var = tk.StringVar(value="No")
away_gets_turnover_cb = ttk.Combobox(main_frame, textvariable=away_gets_turnover_var, 
                                     values=["Yes", "No"], state="readonly")
away_gets_turnover_cb.grid(row=3, column=1, padx=5, pady=2)

home_gets_turnover_var = tk.StringVar(value="No")
home_gets_turnover_cb = ttk.Combobox(main_frame, textvariable=home_gets_turnover_var, 
                                     values=["Yes", "No"], state="readonly")
home_gets_turnover_cb.grid(row=3, column=2, padx=5, pady=2)

# 4) Wins ToP?
ttk.Label(main_frame, text="Wins ToP?").grid(row=4, column=0, sticky=tk.E, pady=2)
away_wins_top_var = tk.StringVar(value="No")
away_wins_top_cb = ttk.Combobox(main_frame, textvariable=away_wins_top_var, 
                                values=["Yes", "No"], state="readonly")
away_wins_top_cb.grid(row=4, column=1, padx=5, pady=2)

home_wins_top_var = tk.StringVar(value="No")
home_wins_top_cb = ttk.Combobox(main_frame, textvariable=home_wins_top_var, 
                                values=["Yes", "No"], state="readonly")
home_wins_top_cb.grid(row=4, column=2, padx=5, pady=2)

# 5) Final Score Approx
ttk.Label(main_frame, text="Final Score Approx:").grid(row=5, column=0, sticky=tk.E, pady=5)
away_score_var = tk.StringVar()
away_score_lbl = ttk.Label(main_frame, textvariable=away_score_var, background="#ffffcc", width=10)
away_score_lbl.grid(row=5, column=1, padx=5, pady=5)

home_score_var = tk.StringVar()
home_score_lbl = ttk.Label(main_frame, textvariable=home_score_var, background="#ffffcc", width=10)
home_score_lbl.grid(row=5, column=2, padx=5, pady=5)

# Calculate and Reset Buttons
calculate_btn = ttk.Button(main_frame, text="Click to Calculate", command=calculate_scores)
calculate_btn.grid(row=6, column=0, columnspan=3, pady=(10, 5))

reset_btn = ttk.Button(main_frame, text="reset", command=reset_fields)
reset_btn.grid(row=7, column=0, columnspan=3, pady=(0, 10))

root.mainloop()
