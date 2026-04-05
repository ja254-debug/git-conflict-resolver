class GitConflictEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        # Starts the world with a conflict in 'main.py'
        self.state = {"conflict": True, "resolved": False, "staged": False, "committed": False}
        return "CONFLICT: main.py has merge conflicts. Use 'git status' to see details."

    def step(self, action_cmd: str):
        cmd = action_cmd.lower().strip()
        reward = 0.0
        done = False

        if "git status" in cmd:
            reward = 0.2
            msg = "Unmerged paths: main.py. Use 'git checkout --ours' to resolve."
        elif "checkout --ours" in cmd:
            self.state["resolved"] = True
            reward = 0.5
            msg = "Conflict resolved! Now 'git add' to stage your changes."
        elif "git add" in cmd and self.state["resolved"]:
            self.state["staged"] = True
            reward = 0.1
            msg = "Changes staged. Now 'git commit' to finish the task."
        elif "git commit" in cmd and self.state["staged"]:
            self.state["committed"] = True
            reward = 0.2
            done = True
            msg = "Task Complete! Merge successful."
        else:
            reward = -0.05
            msg = f"Error: Command '{cmd}' is incorrect at this stage."

        return msg, reward, done