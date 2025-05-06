class WorldModel:
    def __init__(self):
        pass

    def predict(self, state, action):
        """
        Predicts the next state given the current state and action.
        In MVP, this can be a simple grid movement logic.
        """
        # Example: if action is 'up', decrement y-coordinate, etc.
        # This is a placeholder; actual logic depends on the environment.
        return next_state