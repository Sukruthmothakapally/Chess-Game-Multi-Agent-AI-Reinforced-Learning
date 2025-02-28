import chess

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.moves = [] 

    def reset(self):
        self.board.reset()
        self.moves = []

    def apply_move(self, move_uci):
        """
        Attempts to apply a move in UCI format.
        Returns True if the move is legal and successfully applied.
        """
        try:
            move = chess.Move.from_uci(move_uci)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.moves.append(move_uci)
                return True
            else:
                print("Illegal move attempted:", move_uci)
                return False
        except Exception as e:
            print("Error applying move:", e)
            return False

    def is_game_over(self):
        return self.board.is_game_over()

    def result(self):
        return self.board.result()

    def fen(self):
        return self.board.fen()

    def get_board(self):
        return self.board
