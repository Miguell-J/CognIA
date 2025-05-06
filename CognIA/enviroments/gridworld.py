class GridWorld:
    def __init__(self, size, obstacles, goal):
        self.size = size
        self.obstacles = obstacles
        self.goal = goal
        self.agent_position = [0, 0]

    def reset(self):
        self.agent_position = [0, 0]
        return self.agent_position

    def step(self, action):
        # Update agent position based on action
        # Check for obstacles and goal
        # Return new state, reward, and done
        pass