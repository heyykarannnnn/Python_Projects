import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("300x250")  # Increased height to fit the description

        self.player_score = 0
        self.computer_score = 0

        self.player_score_label = tk.Label(self.window, text="Player Score: 0", font=("Arial", 12))
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(self.window, text="Computer Score: 0", font=("Arial", 12))
        self.computer_score_label.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.result_label.pack()

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock 🌎", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT)

        self.paper_button = tk.Button(self.button_frame, text="Paper 📃", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors ✂️", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.description_label = tk.Label(self.window, text="Game Developed By Karan Sethi", font=("Arial", 10))
        self.description_label.pack()  # Added description label

    def play(self, player_move):
        if player_move == "rock":
            player_emoji = "🌎"
        elif player_move == "paper":
            player_emoji = "📃"
        elif player_move == "scissors":
            player_emoji = "✂️"

        computer_move = choice(["rock", "paper", "scissors"])
        if computer_move == "rock":
            computer_emoji = "🌎"
        elif computer_move == "paper":
            computer_emoji = "📃"
        elif computer_move == "scissors":
            computer_emoji = "✂️"

        if player_move == computer_move:
            result = "It's a tie!"
        elif (player_move == "rock" and computer_move == "scissors") or \
             (player_move == "paper" and computer_move == "rock") or \
             (player_move == "scissors" and computer_move == "paper"):
            result = "Player wins!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"Player: {player_emoji}, Computer: {computer_emoji}, {result}")
        self.player_score_label.config(text=f"Player Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.player_score_label.config(text="Player Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()