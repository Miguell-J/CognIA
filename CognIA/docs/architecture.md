# Architecture Overview

The AI Modular Architecture is designed to create a flexible and scalable framework for developing Artificial General Intelligence. The system is composed of several key modules, each responsible for a specific aspect of intelligence.

## Modules

- **Sensorium**: Handles input from the environment, processing multimodal data such as vision, audio, etc.
- **Attention**: Filters and prioritizes sensory data to focus on relevant information.
- **World Model**: Maintains an internal representation of the environment, predicting future states based on current observations and actions.
- **Memory**: Stores past experiences and knowledge, both short-term and long-term.
- **Planner**: Uses the world model and memory to plan actions that achieve goals.
- **Actuators**: Executes actions in the environment based on the planner's decisions.

## Interactions

- The Sensorium captures raw data and passes it to the Attention module.
- Attention filters the data and sends relevant information to the World Model.
- The World Model updates its internal state and shares this with the Planner and Memory.
- Memory stores and retrieves information as needed by the World Model and Planner.
- The Planner uses the World Model and Memory to decide on actions, which are then executed by the Actuators.

For a more detailed description, see the individual module documentation.