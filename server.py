from fastapi import FastAPI
from models import Action, Observation
from environment import GitConflictEnv

app = FastAPI()
env = GitConflictEnv()

@app.post("/reset")
def reset():
    # When the agent starts, it hits this to clear the world
    msg = env.reset()
    return {
        "observation": {
            "terminal_output": msg,
            "is_conflict": True,
            "is_resolved": False,
            "is_committed": False
        }
    }

@app.post("/step")
def step(action: Action):
    # When the agent makes a move, it hits this
    obs_msg, reward, done = env.step(action.command)
    return {
        "observation": {
            "terminal_output": obs_msg,
            "is_conflict": not env.state["resolved"],
            "is_resolved": env.state["resolved"],
            "is_committed": env.state["committed"]
        },
        "reward": reward,
        "done": done
    }

@app.get("/health")
def health():
    return {"status": "ok"}
    