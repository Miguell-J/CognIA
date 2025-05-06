class Actuators:
    def act(self, env, action):
        """
        Executes the action in the environment.
        Returns the new state, reward, and done flag.
        """
        return env.step(action)