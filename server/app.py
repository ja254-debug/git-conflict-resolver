from fastapi import FastAPI
import uvicorn
from models import Action
from environment import GitConflictEnv

app = FastAPI()
env = GitConflictEnv()

@app.post("/reset")
def reset():
    msg = env.reset()
    return {"observation": {"terminal_output": msg, "is_conflict": True, "is_resolved": False, "is_committed": False}}

@app.post("/step")
def step(action: Action):
    obs_msg, reward, done = env.step(action.command)
    return {"observation": {"terminal_output": obs_msg, "is_conflict": not env.state["resolved"], "is_resolved": env.state["resolved"], "is_committed": env.state["committed"]}, "reward": reward, "done": done}

@app.get("/health")
def health():
    return {"status": "ok"}

# THIS IS THE SECTION THE VALIDATOR IS ASKING FOR
def main():
    """Main entry point for the validator to call."""
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
