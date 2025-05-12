from pydantic import BaseModel
from typing import List, Optional

class GameState(BaseModel):
    board: List[int]
    current_player: str
    finished: bool
    winner: Optional[str] = None
