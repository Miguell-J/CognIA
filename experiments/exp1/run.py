import yaml
from src.main import run_mvp

def run_experiment(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    # Set up environment and agent based on config
    # Run the MVP with the configured settings
    run_mvp(config)

if __name__ == "__main__":
    run_experiment('config.yaml')