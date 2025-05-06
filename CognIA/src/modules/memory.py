class Memory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.states = []

    def store(self, state):
        if len(self.states) >= self.capacity:
            self.states.pop(0)
        self.states.append(state)

    def recall(self):
        return self.states