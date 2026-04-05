from pydantic import BaseModel
from typing import List

# This defines what the agent (the AI) can do and see
class Action(BaseModel):
    command: str  # The AI will send strings like "git status"

class Observation(BaseModel):
    terminal_output: str
    is_conflict: bool
    is_resolved: bool
    is_committed: bool

class Reward(BaseModel):
    score: float
    explanation: str