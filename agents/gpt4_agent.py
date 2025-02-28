import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChessMoveResponse(BaseModel):
    move: str = Field(..., description="The move in UCI format, like 'e2e4'.")

def get_gpt4_move(fen: str) -> str:
    """
    Calls OpenAI's GPT-4 API to get a move in UCI format for the given board state (FEN).
    """
    prompt = f"Given the chess board state in FEN: {fen}, provide the best move in UCI format. Only return the move string."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a chess engine that outputs moves in UCI format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=10
        )

        move = response.choices[0].message.content.strip()
        print(f"GPT-4 suggests: {move}")
        return move
    except Exception as e:
        print("Error in GPT-4 agent:", e)
        return None
