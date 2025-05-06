# Minimum Viable Product (MVP)

The MVP focuses on a simplified version of the AI architecture to validate core concepts in a controlled environment.

## Environment

- **GridWorld**: A 2D grid-based environment with obstacles and a goal. The agent must navigate from a starting position to the goal while avoiding obstacles.

## Modules in MVP

- **Sensorium**: Processes the grid state (e.g., agent position, obstacle locations).
- **Attention**: Simplistically focuses on the immediate surroundings of the agent.
- **World Model**: Predicts the next state based on the current state and action.
- **Memory**: Stores recent states to avoid repeated mistakes.
- **Planner**: Uses a basic search algorithm (e.g., A*) to find a path to the goal.
- **Actuators**: Moves the agent in the grid (up, down, left, right).

## Goals

- Validate the interaction between modules.
- Ensure the agent can learn to navigate the grid efficiently.
- Provide a foundation for expanding to more complex modules and environments.