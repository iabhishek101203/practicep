import random
import time

class Agent:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.energy = 10
        self.knowledge = []

    def perceive(self, environment):
        """Observe surroundings"""
        perception = random.choice(environment)
        print(f"{self.name} observes: {perception}")
        return perception

    def decide(self, perception):
        """Decide what to do based on perception and goal"""
        if self.energy <= 0:
            return "rest"
        if self.goal in perception.lower():
            return "analyze"
        return random.choice(["explore", "collect", "think", "rest"])

    def act(self, action):
        """Perform the chosen action"""
        if action == "rest":
            self.energy += 2
            print(f"{self.name} takes a rest. Energy restored to {self.energy}.")
        elif action == "explore":
            self.energy -= 1
            discovery = random.choice(["data", "insight", "pattern"])
            self.knowledge.append(discovery)
            print(f"{self.name} explores and finds {discovery}. Energy: {self.energy}")
        elif action == "collect":
            self.energy -= 2
            print(f"{self.name} collects samples for analysis. Energy: {self.energy}")
        elif action == "analyze":
            self.energy -= 3
            print(f"{self.name} analyzes information about '{self.goal}'. Energy: {self.energy}")
        else:
            print(f"{self.name} thinks deeply... 🤔")

    def run(self, environment, steps=5):
        """Run the agent loop"""
        print(f"🤖 Agent {self.name} begins mission: '{self.goal}'")
        for step in range(steps):
            if self.energy <= 0:
                print(f"{self.name} is too tired to continue.")
                break
            perception = self.perceive(environment)
            action = self.decide(perception)
            self.act(action)
            time.sleep(0.5)
        print(f"🧠 {self.name}'s knowledge: {self.knowledge}")
        print("Mission complete ✅")

# Example environment and run
environment = [
    "A data-rich landscape",
    "An unknown pattern in behavior",
    "A quiet empty field",
    "A potential AI insight",
    "A strange anomaly in the dataset"
]

agent = Agent(name="Astra", goal="insight")
agent.run(environment, steps=7)
