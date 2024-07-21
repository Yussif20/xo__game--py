import tkinter as tk
import random

window = tk.Tk()
window.minsize(width=900, height=700)
window.title("X-O Game")

# Create a frame to act as the container
container = tk.Frame(window)
container.place(relx=0.5, rely=0.5, anchor="center")

# Showing the Score 
player = 0
computer = 0
playerScore = tk.Label(
    container,
    text="You: " + str(player),
    fg="white",
    bg="black",
    font=("Arial", 20),
    width=20,
    height=2
)
computerScore = tk.Label(
    container,
    text="Computer: " + str(computer),
    fg="white",
    bg="black",
    font=("Arial", 20),
    width=20,
    height=2
)

# Add the labels next to each other
playerScore.grid(row=0, column=0, padx=5, pady=10, sticky="e")
computerScore.grid(row=0, column=1, padx=5, pady=10, sticky="w")

# Create a label to display the game result
result_label = tk.Label(
    container,
    text="",
    fg="black",
    font=("Arial", 20),
    width=40,
    height=2
)
result_label.grid(row=1, column=0, columnspan=2, pady=10)

# Create the restart button
def restart_game():
    for game_square in game_squares:
        game_square.config(text="", bg="white")
    result_label.config(text="")

restart_button = tk.Button(
    container,
    text="Restart",
    command=restart_game,
    fg="white",
    bg="red",
    font=("Arial", 20),
    width=20,
    height=2
)
restart_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a frame for the game squares
grid_frame = tk.Frame(container)
grid_frame.grid(row=3, column=0, columnspan=2)

# Function to handle player click
def player_click(event, game_square):
    if game_square.cget("text") == "":
        game_square.config(text="X")
        if check_winner("X"):
            update_score("player")
            result_label.config(text="X Won!")
        elif check_tie():
            result_label.config(text="It's a tie!")
            for sq in game_squares:
                sq.config(bg="red")
        else:
            computer_turn()

# Function for computer to choose a random empty square
def computer_turn():
    empty_squares = [sq for sq in game_squares if sq.cget("text") == ""]
    if empty_squares:
        choice = random.choice(empty_squares)
        choice.config(text="O")
        if check_winner("O"):
            update_score("computer")
            result_label.config(text="O Won!")
        elif check_tie():
            result_label.config(text="It's a tie!")
            for sq in game_squares:
                sq.config(bg="red")

# Function to check for a win
def check_winner(symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(game_squares[i].cget("text") == symbol for i in combo):
            color = "cyan" if symbol == "X" else "red"
            for i in combo:
                game_squares[i].config(bg=color)
            return True
    return False

# Function to check for a tie
def check_tie():
    return all(sq.cget("text") != "" for sq in game_squares)

# Function to update the score
def update_score(winner):
    global player, computer
    if winner == "player":
        player += 1
        playerScore.config(text="You: " + str(player))
    elif winner == "computer":
        computer += 1
        computerScore.config(text="Computer: " + str(computer))

# Create the game squares
game_squares = []
for i in range(3):
    for j in range(3):
        game_square = tk.Button(
            grid_frame,
            text="",
            fg="black",
            bg="white",
            font=("Arial", 24),
            width=5,
            height=2,
            relief="ridge",
            bd=1,
        )
        game_square.grid(row=i, column=j, padx=10, pady=10)
        game_square.bind("<Button-1>", lambda event, sq=game_square: player_click(event, sq))
        game_squares.append(game_square)

window.mainloop()
