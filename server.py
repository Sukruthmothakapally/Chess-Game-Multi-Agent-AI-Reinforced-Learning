import sys
import os
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Add the current directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chess_game import ChessGame
from agents import gpt4_agent, deepseek_agent

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Global objects and settings
game = ChessGame()
TOTAL_GAMES = 1
current_game_number = 0
game_running = False

# Shared state for the UI
current_state = {
    "fen": game.fen(),
    "moves": [],
    "game_number": current_game_number,
    "result": ""
}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/state")
def get_state():
    return current_state

@app.post("/startgame")
async def start_game():
    global game_running
    if not game_running:
        game_running = True
        asyncio.create_task(game_loop())
    return {"message": "Game started"}

async def game_loop():
    global current_game_number, game_running, current_state
    while current_game_number < TOTAL_GAMES:
        game.reset()
        current_state["result"] = ""
        # Play a game until it's over
        while not game.is_game_over():
            # --- GPT-4 (White) Move ---
            fen = game.fen()
            move = gpt4_agent.get_gpt4_move(fen)
            if move is None or not game.apply_move(move):
                import random
                legal_moves = list(game.get_board().legal_moves)
                move = random.choice(legal_moves).uci()
                game.apply_move(move)
            current_state["fen"] = game.fen()
            current_state["moves"] = game.moves
            await asyncio.sleep(0.5)
            if game.is_game_over():
                break

            # --- DeepSeek (Black) Move ---
            fen = game.fen()
            move = deepseek_agent.get_deepseek_move(fen)
            if move is None or not game.apply_move(move):
                import random
                legal_moves = list(game.get_board().legal_moves)
                move = random.choice(legal_moves).uci()
                game.apply_move(move)
            current_state["fen"] = game.fen()
            current_state["moves"] = game.moves
            await asyncio.sleep(0.5)
        
        # End of a game
        result = game.result()  # e.g., "1-0", "0-1", or "1/2-1/2"
        current_state["result"] = result
        current_game_number += 1
        await asyncio.sleep(1)
        current_state["game_number"] = current_game_number

    game_running = False

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
