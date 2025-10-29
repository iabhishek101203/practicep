import random
import time

class GoalAgent:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.position = 0
        self.energy = 10

    def perceive(self):
        """Perceive environment as random events"""
        events = ["clear path", "obstacle", "energy boost", "found clue"]
        event = random.choice(events)
        print(f"👀 {self.name} perceives: {event}")
        return event

    def decide(self, event):
        """Decide next action based on perception"""
        if self.energy <= 0:
            return "rest"
        if event == "obstacle":
            return "jump"
        elif event == "energy boost":
            return "recharge"
        elif event == "found clue":
            return "analyze"
        return "move forward"

    def act(self, action):
        """Perform the action"""
        if action == "move forward":
            self.position += 1
            self.energy -= 1
            print(f"➡️ {self.name} moves forward to position {self.position}. Energy: {self.energy}")
        elif action == "jump":
            self.position += 1
            self.energy -= 2
            print(f"🦘 {self.name} jumps over obstacle! Position: {self.position}, Energy: {self.energy}")
        elif action == "recharge":
            self.energy += 3
            print(f"🔋 {self.name} recharges energy! Energy: {self.energy}")
        elif action == "analyze":
            self.energy -= 1
            print(f"🧠 {self.name} analyzes clue for goal '{self.goal}'. Energy: {self.energy}")
        elif action == "rest":
            self.energy += 2
            print(f"💤 {self.name} rests. Energy: {self.energy}")

    def run(self, steps=8):
        print(f"\n🤖 Agent {self.name} starts goal: '{self.goal}'\n")
        for _ in range(steps):
            if self.position >= 10:
                print(f"🏆 {self.name} reached the goal '{self.goal}'!")
                break
            event = self.perceive()
            action = self.decide(event)
            self.act(action)
            time.sleep(0.5)
        else:
            print(f"❌ {self.name} did not reach the goal. Final position: {self.position}")
        print(f"Final Energy: {self.energy}\n")

# Run the agent
agent = GoalAgent("Orion", "find the hidden AI artifact")
agent.run(steps=12)
