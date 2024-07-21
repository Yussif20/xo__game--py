import tkinter as tk
import random

class TicTacToeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("X-O Game")
        self.master.minsize(width=900, height=700)
        
        self.player_score = 0
        self.computer_score = 0

        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        container = tk.Frame(self.master)
        container.place(relx=0.5, rely=0.5, anchor="center")

        self.player_label = tk.Label(
            container, text=f"You: {self.player_score}", fg="white", bg="black",
            font=("Arial", 20), width=20, height=2
        )
        self.computer_label = tk.Label(
            container, text=f"Computer: {self.computer_score}", fg="white", bg="black",
            font=("Arial", 20), width=20, height=2
        )
        self.player_label.grid(row=0, column=0, padx=5, pady=10, sticky="e")
        self.computer_label.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        self.result_label = tk.Label(
            container, text="", fg="black", font=("Arial", 20), width=40, height=2
        )
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)

        restart_button = tk.Button(
            container, text="Restart", command=self.reset_game, fg="white", bg="red",
            font=("Arial", 20), width=20, height=2
        )
        restart_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.grid_frame = tk.Frame(container)
        self.grid_frame.grid(row=3, column=0, columnspan=2)

        self.game_squares = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    self.grid_frame, text="", fg="black", bg="white", font=("Arial", 24),
                    width=5, height=2, relief="ridge", bd=1,
                    command=lambda i=i, j=j: self.player_click(i, j)
                )
                button.grid(row=i, column=j, padx=10, pady=10)
                row.append(button)
            self.game_squares.append(row)

    def reset_game(self):
        for row in self.game_squares:
            for button in row:
                button.config(text="", bg="white", state=tk.NORMAL)
        self.result_label.config(text="")

    def player_click(self, i, j):
        if self.game_squares[i][j].cget("text") == "":
            self.game_squares[i][j].config(text="X")
            if self.check_winner("X"):
                self.update_score("player")
                self.end_game("X Won!")
            elif self.check_tie():
                self.end_game("It's a tie!")
            else:
                self.computer_turn()

    def computer_turn(self):
        empty_squares = [(i, j) for i in range(3) for j in range(3) if self.game_squares[i][j].cget("text") == ""]
        if empty_squares:
            i, j = random.choice(empty_squares)
            self.game_squares[i][j].config(text="O")
            if self.check_winner("O"):
                self.update_score("computer")
                self.end_game("O Won!")
            elif self.check_tie():
                self.end_game("It's a tie!")

    def check_winner(self, symbol):
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]
        for combo in winning_combinations:
            if all(self.game_squares[i][j].cget("text") == symbol for i, j in combo):
                color = "cyan" if symbol == "X" else "red"
                for i, j in combo:
                    self.game_squares[i][j].config(bg=color)
                return True
        return False

    def check_tie(self):
        return all(self.game_squares[i][j].cget("text") != "" for i in range(3) for j in range(3))

    def update_score(self, winner):
        if winner == "player":
            self.player_score += 1
            self.player_label.config(text=f"You: {self.player_score}")
        elif winner == "computer":
            self.computer_score += 1
            self.computer_label.config(text=f"Computer: {self.computer_score}")

    def end_game(self, message):
        self.result_label.config(text=message)
        for row in self.game_squares:
            for button in row:
                button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
