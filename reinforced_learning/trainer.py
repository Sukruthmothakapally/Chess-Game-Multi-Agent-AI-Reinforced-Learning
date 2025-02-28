class RLTrainer:
    def __init__(self):
        self.results = {"gpt4": 0, "deepseek": 0, "draws": 0}
        self.game_logs = []

    def log_game(self, game_number, moves, winner, final_fen):
        log_entry = {
            "game_number": game_number,
            "moves": moves,
            "winner": winner,
            "final_fen": final_fen
        }
        self.game_logs.append(log_entry)
        print(f"Logged game {game_number}: {log_entry}")

    def update_result(self, winner):
        # In python-chess, "1-0" means white wins (GPT-4), "0-1" means black wins (DeepSeek)
        if winner == "1-0":
            self.results["gpt4"] += 1
        elif winner == "0-1":
            self.results["deepseek"] += 1
        else:
            self.results["draws"] += 1

    def learn_from_game(self, moves, winner):
        """
        Placeholder for reinforcement learning updates.
        In a real implementation, use the game moves and outcome to update the agents' policies.
        """
        print("RL Trainer: Learning from game...")
        pass

    def print_summary(self):
        print("\n--- RL Training Summary ---")
        print("GPT-4 wins:", self.results["gpt4"])
        print("DeepSeek wins:", self.results["deepseek"])
        print("Draws:", self.results["draws"])

    def get_winner(self):
        if self.results["gpt4"] > self.results["deepseek"]:
            return "GPT-4"
        elif self.results["deepseek"] > self.results["gpt4"]:
            return "DeepSeek"
        else:
            return "Draw"
