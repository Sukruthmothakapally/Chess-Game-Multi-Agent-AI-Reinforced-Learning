import csv
import os

class GameLogger:
    def __init__(self, filename="game_logs.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["game_number", "moves", "winner", "final_fen"])

    def log_game(self, game_number, moves, winner, final_fen):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([game_number, " ".join(moves), winner, final_fen])
