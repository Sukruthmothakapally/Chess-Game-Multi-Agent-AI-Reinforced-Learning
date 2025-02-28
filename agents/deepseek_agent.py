import os
import json 
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com" 
)

class ChessMoveResponse(BaseModel):
    move: str = Field(..., description="The move in UCI format, like 'e2e4'.")

def get_deepseek_move(fen: str) -> str:
    """
    Calls DeepSeek's chat API to get a move in UCI format for the given board state (FEN).
    The DeepSeek API is invoked with a system prompt instructing the model to output JSON.
    Expected JSON format: {"move": "<uci_move>"}.
    """
    system_prompt = (
        "You are a chess engine that outputs moves in UCI format as a JSON object. "
        "Return output in the format: {\"move\": \"<uci_move>\"}. "
        "Ensure the move is legal given the provided board state."
    )
    user_prompt = f"Given the chess board state in FEN: {fen}, provide the best move in UCI format as JSON."

    try:
        response = client.chat.completions.create(
            model="deepseek-chat", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
            max_tokens=10
        )

        content = response.choices[0].message.content.strip()
        move_data = json.loads(content) 
        move = move_data.get("move", "").strip()
        
        print(f"DeepSeek suggests: {move}")
        return move
    except Exception as e:
        print("Error in DeepSeek agent:", e)
        return None
