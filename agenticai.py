import random
import time

class SmartAgent:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.energy = 10
        self.memory = {}
        self.success_rate = 0.5  # initial guess of how likely actions are to help

    def observe(self):
        """Agent perceives the environment (randomly generated events)."""
        events = [
            "found raw data",
            "spotted anomaly",
            "noisy environment",
            "new AI paper found",
            "code error detected",
            "discovered pattern"
        ]
        event = random.choice(events)
        print(f"👀 {self.name} observes: {event}")
        return event

    def decide(self, event):
        """Decide next action based on event and internal state."""
        if self.energy <= 0:
            return "rest"
        if "pattern" in event:
            return "analyze"
        if "data" in event:
            return "collect"
        if "error" in event:
            return "debug"
        return random.choice(["think", "explore", "rest"])

    def act(self, action):
        """Perform chosen action and update state."""
        outcomes = {
            "analyze": 3,
            "collect": 2,
            "debug": 4,
            "explore": 2,
            "think": 1,
            "rest": -3
        }
        energy_cost = outcomes.get(action, 1)
        self.energy -= energy_cost if action != "rest" else -energy_cost
        success = random.random() < self.success_rate

        print(f"⚙️ {self.name} performs: {action} (Energy: {self.energy})")
        if success:
            reward = random.choice(["found insight", "improved model", "optimized code"])
            self.memory[action] = self.memory.get(action, 0) + 1
            print(f"✅ Success! {self.name} {reward}.")
            self.success_rate = min(1.0, self.success_rate + 0.05)
        else:
            print(f"❌ {self.name}'s action failed.")
            self.success_rate = max(0.1, self.success_rate - 0.05)

    def run(self, steps=6):
        print(f"\n🤖 Agent {self.name} begins mission: '{self.goal}'\n")
        for _ in range(steps):
            if self.energy <= 0:
                print(f"💤 {self.name} is out of energy.")
                break
            event = self.observe()
            action = self.decide(event)
            self.act(action)
            time.sleep(0.6)
        print(f"\n🧠 {self.name}'s memory: {self.memory}")
        print(f"🔋 Final Energy: {self.energy}")
        print("Mission complete ✅\n")

# Run the agent
agent = SmartAgent("Nova", "discover new ML techniques")
agent.run(steps=8)
