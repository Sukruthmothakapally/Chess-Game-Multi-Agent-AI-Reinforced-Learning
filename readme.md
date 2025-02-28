# Chess RL Multi-Agent Project

This project automatically runs chess games between two AI agents:
- **GPT‑4o Agent**: Uses OpenAI’s GPT‑4o API to make decisions and play chess.
- **DeepSeek Agent**: Uses DeepSeek’s chat API (via the `deepseek-chat` model) to make decisions and play chess.

Both agents play a series of 10 games, learning through Reinforcement Learning (RL) to make better moves after each game. The project determines which agent (OpenAI’s GPT-4 vs DeepSeek) is the best chess player based on win count.

## End Goal:
**Which AI is superior at chess?**  
Will **OpenAI GPT-4** or **DeepSeek** win the most games after 10 rounds? This project evaluates their performance by comparing their moves and learning strategies.

---

## Key Features:
- **Two AI Agents**: GPT‑4o vs DeepSeek playing chess autonomously.
- **Reinforcement Learning**: Both agents learn from each move.
- **10 Automated Games**: Played with no human involvement.
- **Legal Move Enforcement**: Agents make only legal moves.
- **Game History & Visualization**: Every move is logged and the chessboard is rendered for each game.


