# Experiments

## Experiment 1: GridWorld Navigation

### Objective

Test the agent's ability to navigate a simple gridworld to reach a goal while avoiding obstacles.

### Setup

- Environment: 5x5 grid with random obstacles.
- Agent starts at (0,0), goal at (4,4).
- Use the MVP modules.

### Metrics

- Success rate: Percentage of trials where the agent reaches the goal.
- Path efficiency: Compare the agent's path length to the optimal path.
- Learning speed: Number of episodes required to achieve consistent success.

### Expected Outcomes

- The agent should learn to reach the goal in most trials.
- Path efficiency should improve over time.
- The system should demonstrate basic learning and planning capabilities.