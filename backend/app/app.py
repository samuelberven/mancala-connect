# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from backend.app.models import GameState

# app = FastAPI(title="Mancala API", \
# description="A basic API for Mancala game state manipulation.")

# # Enable CORS (optional, useful when connecting from a browser-based frontend)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Todo: in production, set to actual front-end domain
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Create a global game state variable for demonstration.
# game_state = GameState(
#     board=[4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0],
#     current_player="Player 1",
#     finished=False,
#     winner=None,
# )

# @app.get("/")
# async def read_root():
#     return {"message": "Welcome to the Mancala API"}

# @app.get("/state", response_model=GameState)
# async def get_state():
#     """Return the current game state."""
#     return game_state

# @app.post("/move")
# async def make_move(pit_index: int):
#     """
#     Dummy move endpoint.
#     For now, alternates current player.
#     Todo: integrate your move logic from CLI app instead of this stub
#     """
#     if pit_index < 1 or pit_index > 6:
#         raise HTTPException(
# status_code=400, detail="Pit index must be between 1 and 6")

#     # TODO: Replace this with the CLI app-derived move logic.
#     game_state.current_player = (
#         "Player 2" if game_state.current_player == "Player 1" else "Player 1"
#     )

#     return game_state
