from environments.gridworld import GridWorld
from src.modules.sensorium import Sensorium
from src.modules.attention import Attention
from src.modules.world_model import WorldModel
from src.modules.planner import Planner
from src.modules.memory import Memory
from src.modules.actuators import Actuators

def run_mvp():
    # Inicialização
    env = GridWorld(size=5, obstacles=[(2, 2)], goal=(4, 4))
    sensorium = Sensorium()
    attention = Attention()
    world_model = WorldModel()
    memory = Memory(capacity=10)
    planner = Planner()
    actuators = Actuators()

    # Loop principal
    state = env.reset()
    for step in range(100):
        # Percepção
        raw_data = sensorium.perceive(state)
        filtered_data = attention.filter(raw_data)

        # Atualização do modelo de mundo
        world_model.update(filtered_data)
        memory.store(state)

        # Planejamento
        action = planner.plan(world_model, memory, env.goal)
        next_state, reward, done = actuators.act(env, action)

        # Atualização do estado
        state = next_state
        print(f"Step {step}: State={state}, Reward={reward}")

        if done:
            print("Goal reached!")
            break

if __name__ == "__main__":
    run_mvp()