from fastapi import FastAPI, HTTPException
from .mancala import Mancala

app = FastAPI()
game = Mancala()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mancala API (built with FastAPI)"}

@app.get("/state")
async def get_state():
    return {"board": game._board, "current_player": game.current_player}

@app.post("/move/{pit_index}")
async def make_move(pit_index: int):
    result = game.execute_turn(pit_index)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.get("/winner")
async def get_winner():
    return game.return_winner()
